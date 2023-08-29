#!/usr/bin/env python3

import rospy
from simulator.msg import event
import random

class SwitchNode:
    def __init__(self, node_name, modality, split_rate, topic1, topic2, topic1_attribute,node_id):
        self.node_name = node_name
        self.modality = modality
        self.split_rate = split_rate
        self.topic1 = "/" + topic1
        self.topic2 = "/" + topic2
        self.topic1_attribute = topic1_attribute
        self.node_id = node_id

        self.sub = rospy.Subscriber(self.node_name, event, self.switch_callback)
        self.pub1 = rospy.Publisher(self.topic1, event, queue_size=10)
        self.pub2 = rospy.Publisher(self.topic2, event, queue_size=10)

    def switch_callback(self, msg):
        route_list = list(msg.route)
        route_list.append(self.node_id)
        msg.route = route_list

        if self.modality == "split":
            self.split_message(msg)
        elif self.modality == "attribute":
            self.attribute_message(msg)

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

    def attribute_message(self, msg):
        if hasattr(msg, self.topic1_attribute) and getattr(msg, self.topic1_attribute) == True:
            self.pub1.publish(msg)
        else:
            self.pub2.publish(msg)

if __name__ == '__main__':
    rospy.init_node("switch2")

    node_name = rospy.get_param("~node_name", "switch_node")
    modality = rospy.get_param("~modality", "split")
    split_rate = rospy.get_param("~split_rate", 0.5)
    topic1 = rospy.get_param("~topic1", "/topic1")
    topic2 = rospy.get_param("~topic2", "/topic2")
    topic1_attribute = rospy.get_param("~topic1_attribute", "attribute1")
    node_id = rospy.get_param("~node_id", 1)

    switch = SwitchNode(node_name, modality, split_rate, topic1, topic2, topic1_attribute,node_id)
    rospy.spin()
