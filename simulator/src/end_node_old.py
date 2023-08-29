#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from simulator.msg import event
from simulator.msg import loginfo
import time
from datetime import datetime

class EndNode:

    def __init__(self,node_name):
        self.node_name = node_name
        self.received_messages = set()
        self.num_expected_messages = 0
        self.arrived_msgs = 0
        self.all_previous_ids_received = False

        self.log_info_sub = rospy.Subscriber("/log_info", loginfo, self.process_log_info)
        self.event_sub = rospy.Subscriber(self.node_name, event, self.process_event)
        self.type_stats = {}

    def process_log_info(self, msg):
        rospy.loginfo(f"Received log info from node {msg.node_name}")
        if msg.type == "generator":
            self.num_expected_messages += msg.value1  # Assuming value1 stores the number of messages

    
    def process_event(self, msg):
        self.arrived_msgs += 1
        generator_id = msg.generator_id
        event_id = msg.ID
        msg.completed_date = rospy.Time.now()
        msg.compl_time = self.stamp_date()
        # print(msg)
        self.received_messages.add((generator_id, event_id))
        # if self.arrived_msgs == self.num_expected_messages:
        #     self.print_statistics()


        # Update type statistics
        if msg.type in self.type_stats:
            self.type_stats[msg.type]["count"] += 1
            self.type_stats[msg.type]["arrival_times"].append(msg.completed_date-msg.generation_date)
        else:
            self.type_stats[msg.type] = {"count": 1, "arrival_times": [rospy.Time.now().to_sec()]}
        
        if self.arrived_msgs == self.num_expected_messages:
            self.print_statistics()

    def get_unique_generator_ids(self):
        return set([generator_id for generator_id, _ in self.received_messages])

    def stamp_date(self):
        completed_date = rospy.Time.now().to_sec()
        formatted_date = datetime.fromtimestamp(completed_date)
        date_string = formatted_date.strftime('%d-%m-%y %H:%M:%S')
        return date_string

    def format_time(self,seconds):
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        seconds = seconds % 60
        return f"{hours} hours, {minutes} minutes, {seconds:.2f} seconds"

    def print_statistics(self):
        print("All messages received:")
        for generator_id in self.get_unique_generator_ids():
            count = sum([1 for gid, _ in self.received_messages if gid == generator_id])
            print(f"Generator {generator_id}: {count} messages")
        
        print("\nMessage type statistics:")
        for msg_type, stats in self.type_stats.items():
            print(f"Message type: {msg_type}")
            print(f"Total count: {stats['count']}")
            if stats['count'] > 0:
                avg_arrival_time = sum(stats['arrival_times']) / stats['count']
                formatted_avg_time = self.format_time(avg_arrival_time)
                print(f"Average arrival time: {formatted_avg_time}")
            

if __name__ == '__main__':
    node_name = "end_node"
    rospy.init_node(node_name)
    end_node = EndNode(node_name)
    rospy.spin()
