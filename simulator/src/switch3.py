#!/usr/bin/env python3

import rospy
from simulator.msg import event
import random

class Switch():
    def __init__(self, node_name, modality, split_rate_topic1, split_rate_topic2, attribute_topic1, attribute_topic2):
        self.name = node_name
        self.modality = modality
        self.split_rate_topic1 = split_rate_topic1
        self.split_rate_topic2 = split_rate_topic2
        self.attribute_topic1 = attribute_topic1
        self.attribute_topic2 = attribute_topic2

        self.subscriber = rospy.Subscriber(self.name, event, self.process_message)
        self.pub1 = rospy.Publisher("topic1", event, queue_size=10)
        self.pub2 = rospy.Publisher("topic2", event, queue_size=10)
        self.pub3 = rospy.Publisher("topic3", event, queue_size=10)

    def process_message(self, msg):
        if self.modality == "split":
            p = random.random()
            if p < self.split_rate_topic1:
                self.pub1.publish(msg)
            elif p < (self.split_rate_topic1 + self.split_rate_topic2):
                self.pub2.publish(msg)
            else:
                self.pub3.publish(msg)
        elif self.modality == "attribute":
            if msg.attribute1 == self.attribute_topic1:
                self.pub1.publish(msg)
            elif msg.attribute1 == self.attribute_topic2:
                self.pub2.publish(msg)
            else:
                self.pub3.publish(msg)

if __name__ == '__main__':
    rospy.init_node("switch_node")
    node_name = rospy.get_param("~node_name", "switch")
    modality = rospy.get_param("~modality", "split")
    split_rate_topic1 = rospy.get_param("~split_rate_topic1", 0.5)
    split_rate_topic2 = rospy.get_param("~split_rate_topic2", 0.25)
    attribute_topic1 = rospy.get_param("~attribute_topic1", "value1")
    attribute_topic2 = rospy.get_param("~attribute_topic2", "value2")

    switch = Switch(node_name, modality, split_rate_topic1, split_rate_topic2, attribute_topic1, attribute_topic2)

    rospy.spin()

# <node name="switch_node" pkg="simulator" type="switch3.py" output="screen">
#     <param name="node_name" value="switch"/>
#     <param name="modality" value="split"/>
#     <param name="split_rate_topic1" value="0.6"/>
#     <param name="split_rate_topic2" value="0.2"/>
#     <param name="attribute_topic1" value="value1"/>
#     <param name="attribute_topic2" value="value2"/>
# </node>
