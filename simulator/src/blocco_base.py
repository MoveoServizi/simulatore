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
        self.number_of_server = 1
        self.node_id = node_id

        # Valori dinamici
        self.queue_length = 0
        self.queue_list = []

        #topic
        # Create a subscriber
        self.subscriber = rospy.Subscriber(self.topic_queue, event, self.queue)
        # Create a publisher
        self.pub = rospy.Publisher(self.topic_pub, event, queue_size=10)
        self.pub_info = rospy.Publisher("/log_info", loginfo, queue_size=10)

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

    def queue(self, msg):
        route_list = list(msg.route)
        route_list.append(self.node_id)
        msg.route = route_list
        
        if self.max_length != -1:
            if self.queue_length < self.max_length:
                self.queue_length += 1
                self.queue_list.append(msg)
        else:
            self.queue_length += 1
            self.queue_list.append(msg)
        print(self.name, ": adding element, queue: ", self.queue_length)
        
    def server(self, server_number):
        print(self.name, " - server ", server_number, " avviato")
        while not rospy.is_shutdown():
            if self.queue_length > 0:
                current_event = self.queue_list[0]
                self.queue_list.pop(0)
                self.queue_length -= 1

                #print(self.name, " : computing on server", server_number, "...")
                time.sleep(self.server_time)
                
                self.pub.publish(current_event)
                print(self.name, " server ", server_number, ": completed event ",current_event.ID, "  queue ",self.queue_length)

        

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