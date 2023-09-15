#!/usr/bin/env python3
import rospy
from simulator.msg import event
from simulator.msg import cluster
import time

class Cluster():
    def __init__(self,node_name, next_element, modality,cluster_events,cluster_time,speed,next_cluster_topic):
        self.node_name = node_name
        self.next_element = next_element
        self.modality = modality
        self.max_cluster_events = cluster_events
        self.cluster_time = cluster_time /speed
        self.speed = speed
        self.max_length_queue = -1
        
        # Valori dinamici
        self.id_count = 0
        self.queue_length = 0
        self.queue_list = []
        self.cluster_queue_length = 0
        self.cluster_queue_list = []
        self.next_cluster_topic = next_cluster_topic + "_cluster"
        self.sl_cluster_topic = node_name + "_cluster"
        #topic
        # Create a subscriber
        self.subscriber = rospy.Subscriber(self.node_name, event, self.route_modality) 
        self.subscriber = rospy.Subscriber(self.sl_cluster_topic, cluster, self.cluster_queue)
        # Create a publisher
        self.pub = rospy.Publisher(self.next_element, event, queue_size=50)
        self.pub_cluster = rospy.Publisher(self.next_cluster_topic, cluster, queue_size=50)
        
    
    def route_modality(self,msg):
        if self.modality == "dividi":
            if msg.type == "cluster":
                self.devide_cluster(msg.ID)
            else:
                self.pub.publish(msg) # trasparente se non un cluster
        else:
            self.queue(msg)
    
    
    
    
    def queue(self, msg):
        
        if self.max_length_queue != -1:
            if self.queue_length < self.max_length_queue:
                self.queue_length += 1
                self.queue_list.append(msg)
                self.create_cluster()
        else:
            self.queue_length += 1
            self.queue_list.append(msg)
            self.create_cluster()
    
    def cluster_queue(self, msg):
            self.cluster_queue_length += 1
            self.cluster_queue_list.append(msg)
            if self.modality == "unisci":
                print("Errore")
        
    def devide_cluster(self, ID):
        if self.cluster_queue_length > 0:
            for i in range(len(self.cluster_queue_list)):
                if self.cluster_queue_list[i].cluster_id == ID:    
                    current_cluster= self.cluster_queue_list[i]
                    self.cluster_queue_list.pop(i)
                    self.cluster_queue_length -= 1
                    size = len(current_cluster.events)
                    if size > 0:
                        for event in current_cluster.events:
                            self.pub.publish(event)
                        print("Cluster diviso in", size, "messaggi")
                    else:
                        print("Errore - cluster vuoto")
                    break
    
    def create_cluster(self):
        size = -1
        if self.cluster_time > 0:
            time.sleep(self.cluster_time)
            size = min(self.max_cluster_events, self.queue_length)
            
        else:
            if self.queue_length >= self.max_cluster_events:
                size = self.max_cluster_events
        
        if size != -1:  
            
            self.id_count += 1
            
            event_flag_cluster =  event()
            event_flag_cluster.generator_id = self.node_name
            event_flag_cluster.type = "cluster"
            event_flag_cluster.ID = self.id_count
            
            cluster_msg = cluster()
            cluster_msg.cluster_id = self.id_count
            cluster_msg.size = size
            
            for i in range(size):
                current_msg= self.queue_list[0]
                self.queue_list.pop(0)
                self.queue_length -= 1
                cluster_msg.events.append(current_msg)
                
            self.pub_cluster.publish(cluster_msg)
            self.pub.publish(event_flag_cluster )
            print("new cluster - size: ", size)



if __name__ == '__main__':
    
    # Initialize the ROS node
    rospy.init_node(rospy.get_param("~node_name", "cluster_node"))
    
    # Get the parameters from the launch file
    node_name = rospy.get_param("~node_name", "cluster_node")
    next_element = rospy.get_param("~next_element", "next_element_topic")
    modality = rospy.get_param("~modality", "events")
    cluster_events = rospy.get_param("~cluster_events", 1)
    cluster_time = rospy.get_param("~cluster_time", -1)
    speed = rospy.get_param("~speed", 1)
    next_cluster_topic = rospy.get_param("~next_cluster_topic","cluster_next")
    # Create an instance of the Coda class with parameters from the launch file
    coda = Cluster(node_name, next_element, modality,cluster_events,cluster_time,speed,next_cluster_topic)
    
    
    
   
    # Spin ROS node
    rospy.spin()