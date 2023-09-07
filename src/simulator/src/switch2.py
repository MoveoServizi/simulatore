#!/usr/bin/env python3

import rospy
from simulator.msg import event
from simulator.msg import loginfo
import random

class SwitchNode:
    def __init__(self, node_name, modality, split_rate, topic1, topic2, split_attribute,attribute_num,node_id):
        self.node_name = node_name
        self.modality = modality
        self.split_rate = split_rate
        self.topic1 = "/" + topic1
        self.topic2 = "/" + topic2
        self.split_attribute = split_attribute
        self.attribute_num = attribute_num
        self.node_id = node_id

        self.sub = rospy.Subscriber(self.node_name, event, self.switch_callback)
        self.pub1 = rospy.Publisher(self.topic1, event, queue_size=50)
        self.pub2 = rospy.Publisher(self.topic2, event, queue_size=50)
        self.log_info_sub = rospy.Subscriber("/log_info", loginfo, self.process_log_info)

    def switch_callback(self, msg):
        route_list = list(msg.route)
        route_list.append(self.node_name)
        print(self.node_name, " ricevuto msg ", msg.ID)

        if self.modality == "split":
            self.split_message(msg)
        elif self.modality == "type":
            self.type_message(msg)
        elif self.modality == "attribute":
            self.attribute_message(msg,self.split_attribute,self.attribute_num)
        elif self.modality == "split_attribute":
            self.attribute_split_message(msg,self.split_attribute,self.attribute_num)

    def split_message(self, msg):
        if self.split_rate <= 0.0:
            self.pub2.publish(msg)
        elif self.split_rate >= 1.0:
            self.pub1.publish(msg)
        else:
            p = random.random()  # Generate a random number between 0 and 1
            if p < self.split_rate:
                self.pub1.publish(msg)
            else:
                self.pub2.publish(msg)

    def type_message(self, msg):
        if msg.type == self.split_attribute:
            self.pub1.publish(msg)
        else:
            self.pub2.publish(msg)
            
    def attribute_message(self, msg, attribute, attribute_num):
        if attribute_num == 1:
            attribute_name = 'split_attribute1'
        elif attribute_num == 2:
            attribute_name = 'split_attribute2'
        elif attribute_num == 3:
            attribute_name = 'split_attribute3'

        if hasattr(msg, attribute_name):

            
            if getattr(msg, attribute_name) == attribute:
                self.pub1.publish(msg)
            else:
                self.pub2.publish(msg)
        else:
            print("ERRORE split non trovato")
            self.split_message(msg)
                
    def attribute_split_message(self, msg,attribute, attribute_num):
        if attribute_num == 1:
            attribute_name = 'split_attribute1'
            split_name = 'split1'
        elif attribute_num == 2:
            attribute_name = 'split_attribute2'
            split_name = 'split2'
        elif attribute_num == 3:
            attribute_name = 'split_attribute3'
            split_name = 'split3'
        else:
            raise ValueError("Invalid attribute number")

        if getattr(msg, attribute_name) == attribute:
            att_split_rate = getattr(msg, split_name)
            p = random.random()  # Generate a random number between 0 and 1
            if p < att_split_rate:
                self.pub1.publish(msg)
            else:
                self.pub2.publish(msg)
        else:
            print("ERRORE split non trovato")
            self.split_message(msg)
    
    def process_log_info(self,msg):
        if msg.type == "end_node":
            if msg.stop_esecution == True:
                rospy.signal_shutdown('Chiusura dello switch')  

if __name__ == '__main__':
    rospy.init_node("switch2")

    node_name = rospy.get_param("~node_name", "switch_node")
    modality = rospy.get_param("~modality", "split")
    split_rate = rospy.get_param("~split_rate", 0.5)
    topic1 = rospy.get_param("~topic1", "/topic1")
    topic2 = rospy.get_param("~topic2", "/topic2")
    topic1_attribute = rospy.get_param("~split_attribute", "split_attribute1")
    attribute_num = rospy.get_param("~attribute_num",1)
    node_id = rospy.get_param("~node_id", 1)

    switch = SwitchNode(node_name, modality, split_rate, topic1, topic2, topic1_attribute,attribute_num,node_id)
    rospy.spin()
