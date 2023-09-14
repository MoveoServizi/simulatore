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
import datetime
import numpy as np

class Coda():
    def __init__(self,node_name,next_element, num_servers, server_time, node_id, speed,uncertanity):
        # Valori configurazione
        self.name = node_name
        self.topic_queue = "/" + node_name
        self.topic_pub = "/" + next_element
        self.max_length = -1
        self.server_time = server_time/speed
        self.server_time_distribution = 0
        self.number_of_server =  num_servers
        self.node_id = node_id
        self.speed = speed
        self.uncertanity = uncertanity
        self.event_complete  = 0
        self.running = True
        self.record_stat = False

        # Valori dinamici
        self.queue_length = 0
        self.queue_list = []
            #calcolo utilizzo
        self.first_arrival_time = None
        self.last_arrival_time = None
        self.total_arrival_events = 0
        self.time_interval = self.server_time * 5
        self.utilization_intervals = []
        self.queue_length_intervals = []
        self.time_array = []
        self.time_array_intervals = []
        self.server_occupancy = [False] *int(num_servers)
        self.occupancy_lock = threading.Lock()  # Per garantire l'accesso sincronizzato
        self.utilization_array = []

        #topic
        # Create a subscriber
        self.subscriber = rospy.Subscriber(self.topic_queue, event, self.queue)
        # Create a publisher
        self.pub = rospy.Publisher(self.topic_pub, event, queue_size=50)
        self.pub_info = rospy.Publisher("/log_info", loginfo, queue_size=50)
        self.log_info_sub = rospy.Subscriber("/log_info", loginfo, self.process_log_info)

        time.sleep(2)
        info_msg =loginfo()
        info_msg.ID_node = node_id
        info_msg.type = "coda"
        info_msg.node_name = node_name
        info_msg.ready = False
        self.pub_info.publish(info_msg)

        
        
        print(self.name, "-  avviamento servers")
        # Launch servers
        server_threads = []
        for server_number in range(1, num_servers + 1):
            server_thread_instance = threading.Thread(target=self.server, args=(server_number,))
            server_threads.append(server_thread_instance)
            server_thread_instance.start()
        
        #lauch computation of utilization
        self.occupancy_monitor_thread = threading.Thread(target=self.monitor_occupancy)
        self.occupancy_monitor_thread.start()
        
        time.sleep(5)
        print(self.name, "-  pronta")
        info_msg =loginfo()
        info_msg.ID_node = node_id
        info_msg.type = "coda"
        info_msg.node_name = node_name
        info_msg.ready = True
        self.pub_info.publish(info_msg)

    def process_log_info(self,msg):
        
        if msg.type == "end_node":
            if msg.stop_esecution == True:
                info_msg =loginfo()
                info_msg.ID_node = self.node_id
                info_msg.type = "coda"
                info_msg.node_name = self.name
                info_msg.info = "test info"
                info_msg.num_servers = self.number_of_server
                info_msg.server_time = self.server_time*self.speed
                info_msg.utiliz_tot = self.get_general_utilization()
                info_msg.utiliz_array = self.get_interval_utilizations()
                info_msg.utiliz_array_tot = self.utilization_array
                info_msg.time_array = self.time_array
                info_msg.time_array_intervals = self.time_array_intervals
                info_msg.queue_array = self.queue_length_intervals
                info_msg.statistic = True
                info_msg.queue_left = self.queue_length
                info_msg.event_processed = self.event_complete
                self.pub_info.publish(info_msg)
                self.running =  False
                rospy.signal_shutdown('Chiusura della coda')
            if msg.start_esecution:
                self.record_stat = True


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
        util = round(utilization,2)
        return util
    
    def get_interval_utilizations(self):
        return self.utilization_intervals
    

    def server(self, server_number):
        print(self.name, " - server ", server_number, " avviato")
        

        while self.running:
            #controlla lista eventi attivi
            #per ogni evento controlla se è scaduto il tempo, nel caso invialo con le funzioni
            self.event_complete += 1
            self.pub.publish(current_event)
            with self.occupancy_lock:
                    self.server_occupancy[server_number - 1] = False
            print(self.name, " server ", server_number, ": completed event ", current_event.ID, "  queue ", self.queue_length, "event commplete ", self.event_complete)
            
            #poi libera un posto nella lista
            
            if self.queue_length > 0 # e se c'è posto nella lista :
                current_event = self.queue_list[0]
                self.queue_list.pop(0)
                self.queue_length -= 1
                with self.occupancy_lock:
                    self.server_occupancy[server_number - 1] = True
                
                if self.uncertanity:
                    # Pattern: Exponential distribution
                    mu = 1/self.server_time
                    dt = -1/mu * np.log(1 - np.random.rand())
                else:
                    dt = self.server_time
                
                #aggiungi evento alla lista aggiungendo il suo dt
                # pensabo tipo a time.now +dt
                
                
    def monitor_occupancy(self):
        cicle_max = max(1,round(self.time_interval/self.server_time/2))
        cicle = 0

        while not rospy.is_shutdown():
            if self.record_stat:
                # Dormi per mezzo self.server_time prima di registrare lo stato di occupazione
                time.sleep(self.server_time / 2)
                
                with self.occupancy_lock:
                    if cicle == 0:
                        server_occupied_counts = [0] * num_servers

                    # Calcola l'utilizzazione in base allo stato di occupazione dei server
                    for server_number in range(num_servers):
                        if self.server_occupancy[server_number]:
                            server_occupied_counts[server_number] += 1
                
                self.utilization_array.append(min(self.get_general_utilization(),1))
                self.queue_length_intervals.append(self.queue_length)
                self.time_array.append(rospy.Time.now())
                cicle += 1
                # Calcola l'utilizzazione nei vari intervalli di tempo
                if cicle == cicle_max:
                    utilization = sum(server_occupied_counts) / (num_servers * cicle_max)
                    util =round(utilization,2)
                    self.utilization_intervals.append(util)
                    #self.queue_length_intervals.append(self.queue_length)
                    self.time_array_intervals.append(rospy.Time.now())
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
    speed = rospy.get_param("~speed", 1)
    uncertanity = rospy.get_param("~uncertanity", "False")
    # Create an instance of the Coda class with parameters from the launch file
    coda = Coda(node_name, next_element, num_servers,server_time,node_id, speed,uncertanity)
    
    
    
   
    # Spin ROS node
    rospy.spin()