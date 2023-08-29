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
        self.node_passing_stats = {}  # Dizionario per tenere traccia delle statistiche di passaggio per ogni nodo

        self.log_info_sub = rospy.Subscriber("/log_info", loginfo, self.process_log_info)
        self.event_sub = rospy.Subscriber(self.node_name, event, self.process_event)
        self.pub_info = rospy.Publisher("/log_info", loginfo, queue_size=10)
        self.type_stats = {}
        self.data_by_type = {}

    def process_log_info(self, msg):
        rospy.loginfo(f"Received log info from node {msg.node_name}")
        if msg.type == "generator":
            self.num_expected_messages += msg.value1  # Assuming value1 stores the number of messages
        if msg.flag2 == True:
            data = {
            "node_name": msg.node_name,
            "value1": round(msg.value1,2),
            "value2": [round(number, 2) for number in msg.value2],
            "attribute": msg.attribute1
            }
            msg_type = msg.type
            if msg_type not in self.data_by_type:
                self.data_by_type[msg_type] = []

            self.data_by_type[msg_type].append(data)

    
    def process_event(self, msg):
        self.arrived_msgs += 1
        generator_id = msg.generator_id
        event_id = msg.ID
        msg.completed_date = rospy.Time.now()
        msg.compl_time = self.stamp_date()
        self.received_messages.add((generator_id, event_id))



        # Update type statistics
        if msg.type in self.type_stats:
            self.type_stats[msg.type]["count"] += 1
            spend_time = msg.completed_date-msg.generation_date
            self.type_stats[msg.type]["arrival_times"].append(spend_time)
        else:
            spend_time = msg.completed_date-msg.generation_date
            self.type_stats[msg.type] = {"count": 1, "arrival_times": [spend_time]}
        
        # Update node passing statistics
        for node_id in msg.route:
            if msg.type in self.node_passing_stats:
                if node_id in self.node_passing_stats[msg.type]:
                    self.node_passing_stats[msg.type][node_id] += 1
                else:
                    self.node_passing_stats[msg.type][node_id] = 1
            else:
                self.node_passing_stats[msg.type] = {node_id: 1}
        
        if self.arrived_msgs == self.num_expected_messages:
            info_msg =loginfo()
            
            info_msg.type = "end_node"
            info_msg.node_name = self.node_name
            info_msg.flag1 = True
            self.pub_info.publish(info_msg)
            time.sleep(5)
            self.print_statistics()
            self.print_data_by_type()

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


    def print_data_by_type(self):
        for msg_type, data_list in self.data_by_type.items():
            print(f"Type {msg_type}:\n")
            for data in data_list:
                print(f"node_name: {data['node_name']}")
                print(f"utilizzazione totale: {data['value1']}")
                print(f"utilizzazione: {data['value2']}")
                print(f"attribute: {data['attribute']}")
                print("\n")


    def print_statistics(self):
        print("All messages received:")
        for generator_id in self.get_unique_generator_ids():
            count = sum([1 for gid, _ in self.received_messages if gid == generator_id])
            print(f"Generator {generator_id}: {count} messages")

            
        print("\nMessage type statistics:")
        for msg_type, stats in self.type_stats.items():
            print(f"\nMessage type: {msg_type}")
            print(f"Total count: {stats['count']}")
            if stats['count'] > 0:
                total_time = sum([t.to_sec() for t in stats['arrival_times']])
                avg_arrival_time = total_time / stats['count']
                formatted_avg_time = self.format_time(avg_arrival_time)
                print(f"Average arrival time: {formatted_avg_time}")
                
            passing_stats = self.node_passing_stats.get(msg_type, {})
            total_passing_events = stats['count']
            #print("\nNode passing statistics:")
            for node_id, passing_count in passing_stats.items():
                passing_percentage = (passing_count / total_passing_events) * 100
                print(f"Node {node_id}: {passing_percentage:.2f}%")
            

if __name__ == '__main__':
    node_name = "end_node"
    rospy.init_node(node_name)
    end_node = EndNode(node_name)
    rospy.spin()
