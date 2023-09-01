#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from simulator.msg import event
from simulator.msg import loginfo
import time
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np

class EndNode:

    def __init__(self,node_name,modality,stop_time):
        self.modality = modality
        self.stop_time = stop_time
        self.node_name = node_name
        self.received_messages = set()
        self.num_expected_messages = 0
        self.arrived_msgs = 0
        self.all_previous_ids_received = False
        self.node_passing_stats = {}  # Dizionario per tenere traccia delle statistiche di passaggio per ogni nodo
        self.start = rospy.Time.now()

        self.log_info_sub = rospy.Subscriber("/log_info", loginfo, self.process_log_info)
        self.event_sub = rospy.Subscriber(self.node_name, event, self.process_event)
        self.pub_info = rospy.Publisher("/log_info", loginfo, queue_size=20)
        self.type_stats = {}
        self.data_by_type = {}

    
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

        #stop condition
        if self.modality == "events":
            if self.arrived_msgs == self.num_expected_messages:
                self.total_seconds = rospy.Time.now().to_sec() - self.start.to_sec()
                self.print_result()
        elif self.modality == "time":
            self.total_seconds = rospy.Time.now().to_sec() - self.start.to_sec()
            if self.total_seconds > self.stop_time:
                print("TIME IS OVER!!!")
                self.print_result()
            
    
    
    def process_log_info(self, msg):
        rospy.loginfo(f"Received log info from node {msg.node_name}")
        if msg.type == "generator":
            self.num_expected_messages += msg.events_left  # Assuming value1 stores the number of messages
        if msg.statistic == True and msg.type == "coda":
            data = {
            "node_name": msg.node_name,
            "utiliz_tot": round(msg.utiliz_tot,2),
            "utiliz_array": [round(number, 2) for number in msg.utiliz_array],
            "info": msg.info,
            "queue_length": msg.queue_array,
            "time_array" : msg.time_array
            }
            msg_type = msg.type
            if msg_type not in self.data_by_type:
                self.data_by_type[msg_type] = []

            self.data_by_type[msg_type].append(data)
 

    def print_result(self):
        info_msg =loginfo()
            
        info_msg.type = "end_node"
        info_msg.node_name = self.node_name
        info_msg.stop_esecution = True
        self.pub_info.publish(info_msg)
        time.sleep(5)
        self.print_statistics()
        self.print_data_by_type()
        

    def print_statistics(self):
        print("################  STATISTIC ############")
        print("total esecution time: ", str(self.total_seconds))
        print("events recived:")
        for generator_id in self.get_unique_generator_ids():
            count = sum([1 for gid, _ in self.received_messages if gid == generator_id])
            print(f"Generator {generator_id}: {count} messages")

            
        print("\nRoute of events:")
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
                
    def print_data_by_type(self):
        for msg_type, data_list in self.data_by_type.items():
            print(f"Type {msg_type}:\n")
            for data in data_list:
                print(f"node_name: {data['node_name']}")
                print(f"utilizzazione totale: {data['utiliz_tot']}")
                print(f"utilizzazione: {data['utiliz_array']}")
                print(f"info: {data['info']}")
                print("\n")
                
                self.plot_temporal_data(data['queue_length'],data['utiliz_array'],data['time_array'],data['node_name'])
                
    def plot_temporal_data(self,values1, values2,time_array, title):
        time_steps = [(time.to_sec() - self.start.to_sec()) for time in time_array]
        
        # Creazione della griglia con 1 riga e 2 colonne per i subplot
        plt.figure(figsize=(10, 5))  # Imposta le dimensioni della figura
        plt.subplot(1, 2, 1)  # Primo subplot
        plt.plot(time_steps, values1, marker='*')
        plt.title('Lunghezza coda')
        plt.xlabel('Tempo')
        plt.ylabel('entità in coda')
        plt.grid(True)
        
        plt.subplot(1, 2, 2)  # Secondo subplot
        plt.plot(time_steps, values2, marker='*', color='m')
        plt.title('Utilizzazione')
        plt.xlabel('Tempo')
        plt.ylabel('percentuale di utilizzazione')
        plt.grid(True)
        
        plt.suptitle(title)  # Titolo dell'intera figura
        plt.tight_layout()   # Ottimizza la disposizione dei subplot
        plt.show()
        plt.pause(0.001)
       
        
    ##funzioni di servizio
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





if __name__ == '__main__':
    rospy.init_node(rospy.get_param("~node_name", "end_node"))
    node_name = rospy.get_param("~node_name", "end_node")
    modality = rospy.get_param("~modality", "events")
    stop_time = rospy.get_param("~stop_time", 540)
    plt.ion()
    
    end_node = EndNode(node_name,modality,stop_time)
    rospy.spin()
    