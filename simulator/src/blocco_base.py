#!/usr/bin/env python3

# elemento base del simulatore. coda M/M/n
# questp elemento è composto da due parti, la prima è la coda di eventi che si accumulano, la seconda è il server che elabora gli eventi.
# la coda è un puro elemento di accumolo, può avere capacità illimitata o limitata.
# il server elabora il singolo evento in una certa quantità di tempo, questa può essere fissa, seguire un distribuzione (poisson), dipendere da parametri esterni o da parametri intrinsechi dell'evento da elaborare.
# ci possono essere più server in parallelo per ogni singola coda. Ogni server può indirizzare gli elementi elaborati a uno o più code successive.
import rospy
from simulator.msg import event
from simulator.msg import loginfo
import threading
import time
import logging

class Coda():
    def __init__(self,node_name,next_element, num_servers, server_time, node_id):
        # Valori configurazione
        self.name = node_name
        self.topic_queue = "/" + node_name
        self.topic_pub = "/" + next_element
        self.max_length = -1
        self.server_time = server_time
        self.server_time_distribution = 0
        self.number_of_server =  num_servers
        self.node_id = node_id

        # Valori dinamici
        self.queue_length = 0
        self.queue_list = []
            #calcolo utilizzo
        self.first_arrival_time = None
        self.last_arrival_time = None
        self.total_arrival_events = 0
        self.time_interval = 2 #self.server_time * 10
        self.utilization_intervals = []
        self.queue_length_intervals = []
        self.server_occupancy = [False] *int(num_servers)
        self.occupancy_lock = threading.Lock()  # Per garantire l'accesso sincronizzato

        #topic
        # Create a subscriber
        self.subscriber = rospy.Subscriber(self.topic_queue, event, self.queue)
        # Create a publisher
        self.pub = rospy.Publisher(self.topic_pub, event, queue_size=10)
        self.pub_info = rospy.Publisher("/log_info", loginfo, queue_size=20)
        self.log_info_sub = rospy.Subscriber("/log_info", loginfo, self.process_log_info)

        time.sleep(5)
        info_msg =loginfo()
        info_msg.ID_node = node_id
        info_msg.type = "coda"
        info_msg.node_name = node_name
        self.pub_info.publish(info_msg)

        # Launch servers
        server_threads = []
        for server_number in range(1, num_servers + 1):
            server_thread_instance = threading.Thread(target=self.server, args=(server_number,))
            server_threads.append(server_thread_instance)
            server_thread_instance.start()

        #lauch computation of utilization
        self.occupancy_monitor_thread = threading.Thread(target=self.monitor_occupancy)
        self.occupancy_monitor_thread.start()

    def process_log_info(self,msg):
        if msg.type == "end_node":
            if msg.flag1 == True:
                info_msg =loginfo()
                info_msg.ID_node = node_id
                info_msg.type = "coda"
                info_msg.node_name = node_name
                info_msg.attribute1 = "test info"
                info_msg.value1 = self.get_general_utilization()
                info_msg.value2 = self.get_interval_utilizations()
                info_msg.value3 = self.time_interval
                info_msg.value4 = self.queue_length_intervals
                info_msg.flag2 = True
                self.pub_info.publish(info_msg)
                rospy.signal_shutdown('Chiusura del launcher_node')


    def queue(self, msg):
        route_list = list(msg.route)
        route_list.append(self.name)
        msg.route = route_list

        # Calcola l'utilizzazione generale al momento dell'arrivo di un evento
        if self.first_arrival_time is None:
            self.first_arrival_time = rospy.Time.now()
        
        self.last_arrival_time = rospy.Time.now()
        self.total_arrival_events += 1
        
        if self.max_length != -1:
            if self.queue_length < self.max_length:
                self.queue_length += 1
                self.queue_list.append(msg)
        else:
            self.queue_length += 1
            self.queue_list.append(msg)
        print(self.name, ": adding element, queue: ", self.queue_length)
        

    def get_general_utilization(self):
        if self.first_arrival_time is None or self.last_arrival_time is None:
            return 0.0
        
        total_time = (self.last_arrival_time - self.first_arrival_time).to_sec()
        

        utilization = (self.total_arrival_events/total_time) / (self.number_of_server * (1/self.server_time))
        print_line = self.name+" "+str(self.total_arrival_events)+ " " +str(total_time) +  " " +str(self.number_of_server * 1/self.server_time)+ " = " + str(utilization)
        print(print_line)
        util = round(utilization,2)
        return util
    def get_interval_utilizations(self):
        return self.utilization_intervals
    

    def server(self, server_number):
        print(self.name, " - server ", server_number, " avviato")
        

        while not rospy.is_shutdown():
            if self.queue_length > 0:
                current_event = self.queue_list[0]
                self.queue_list.pop(0)
                self.queue_length -= 1
                with self.occupancy_lock:
                    self.server_occupancy[server_number - 1] = True
                
                #print(self.name, " : computing on server", server_number, "...")
                time.sleep(self.server_time)
                
                self.pub.publish(current_event)
                with self.occupancy_lock:
                    self.server_occupancy[server_number - 1] = False
                print(self.name, " server ", server_number, ": completed event ", current_event.ID, "  queue ", self.queue_length)
            
    def monitor_occupancy(self):
        cicle_max = max(1,round(self.time_interval/self.server_time/2))
        cicle = 0
        while not rospy.is_shutdown():
            # Dormi per mezzo self.server_time prima di registrare lo stato di occupazione
            time.sleep(self.server_time / 2)
            
            with self.occupancy_lock:
                if cicle == 0:
                    server_occupied_counts = [0] * num_servers

                # Calcola l'utilizzazione in base allo stato di occupazione dei server
                for server_number in range(num_servers):
                    if self.server_occupancy[server_number]:
                        server_occupied_counts[server_number] += 1

            cicle += 1
            # Calcola l'utilizzazione nei vari intervalli di tempo
            if cicle == cicle_max:
                utilization = sum(server_occupied_counts) / (num_servers * cicle_max)
                util =round(utilization,2)
                self.utilization_intervals.append(util)
                self.queue_length_intervals.append(self.queue_length)
                cicle = 0


if __name__ == '__main__':
    
    # Initialize the ROS node
    rospy.init_node(rospy.get_param("~node_name", "coda_node"))
    
    # Get the parameters from the launch file
    node_name = rospy.get_param("~node_name", "coda_node")
    next_element = rospy.get_param("~next_element", "next_element_topic")
    num_servers = rospy.get_param("~num_servers", 1)
    server_time = rospy.get_param("~server_time", 2)
    node_id = rospy.get_param("~node_id", 1)
    # Create an instance of the Coda class with parameters from the launch file
    coda1 = Coda(node_name, next_element, num_servers, server_time,node_id)

   
    # Spin ROS node
    rospy.spin()