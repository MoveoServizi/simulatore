#!/usr/bin/env python3

#genera gli eventi

import rospy
from simulator.msg import event
from simulator.msg import loginfo
import time
from datetime import datetime

class GeneratorNode:
    def __init__(self, node_name, next_element, gen_freq, num_messages, event_type, node_id,attribute1,value1):
        self.node_name = node_name
        self.next_element = "/" + next_element
        self.gen_freq = gen_freq
        self.num_messages = num_messages
        self.event_type = event_type
        self.event_id = 1
        self.attribute1 = attribute1
        self.value1 = value1

        self.pub = rospy.Publisher(self.next_element, event, queue_size=10)
        self.pub_info = rospy.Publisher("/log_info", loginfo, queue_size=10)
        self.log_info_sub = rospy.Subscriber("/log_info", loginfo, self.process_log_info)
        
        time.sleep(1)
        info_msg =loginfo()
        info_msg.ID_node = node_id
        info_msg.type = "generator"
        info_msg.node_name = node_name
        info_msg.events_left = num_messages
        self.pub_info.publish(info_msg)

    def generate_messages(self):
        
        rospy.loginfo(f"{self.node_name}: Generating {self.num_messages} messages...")
        i = 0
        while not rospy.is_shutdown():
            if i < self.num_messages:
                event_msg = event()
                event_msg.ID = self.event_id
                event_msg.generator_id = self.node_name
                event_msg.type = self.event_type
                event_msg.route = [self.node_name]
                event_msg.last_event = False
                event_msg.generation_date = rospy.Time.now()
                event_msg.gen_time = self.stamp_date()
                
                event_msg.split_attribute1 = self.attribute1
                event_msg.split1 = self.value1
                
                
                if i == self.num_messages - 1:
                    event_msg.last_event = True
                self.pub.publish(event_msg)
                self.event_id += 1
                i += 1
                rospy.loginfo(f"{self.node_name}: Published event ID {event_msg.ID}")
                time.sleep(1 / self.gen_freq)

    def stamp_date(self):
        completed_date = rospy.Time.now().to_sec()  # Ottieni il timestamp in secondi
        # Crea un oggetto datetime dalla data formattata
        formatted_date = datetime.fromtimestamp(completed_date)
        # Formatta la data secondo il tuo formato desiderato
        date_string = formatted_date.strftime('%d-%m-%y %H:%M:%S')
        return date_string
    
    def process_log_info(self,msg):
        if msg.type == "end_node":
            if msg.stop_esecution == True:
                info_msg =loginfo()
                info_msg.type = "generator"
                info_msg.node_name = self.node_name
                info_msg.events_left = self.num_messages - self.event_id
                info_msg.statistic = True
                self.pub_info.publish(info_msg)
                rospy.signal_shutdown('Chiusura generatore') 
    
    

if __name__ == '__main__':
    rospy.init_node(rospy.get_param("~node_name", "generator"))
    node_id = rospy.get_param("~node_id", 1)
    node_name = rospy.get_param("~node_name", "generator")
    next_element = rospy.get_param("~next_element", "next_element")
    gen_freq = rospy.get_param("~gen_freq", 1.0)
    num_messages = rospy.get_param("~num_messages", 10)
    event_type = rospy.get_param("~event_type", "evento_semplice")
    
    attribute1 = rospy.get_param("~split_attribute1", "-")
    value1 = rospy.get_param("~value1", "0.0")

    generator = GeneratorNode(node_name, next_element, gen_freq, num_messages, event_type, node_id,attribute1,value1)
    generator.generate_messages()
