#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from simulator.msg import event
from simulator.msg import loginfo
import time
from datetime import datetime
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import sys
import os
import signal
import subprocess

class EndNode:

    def __init__(self,node_name,modality,stop_time,speed,file_name):
        self.modality = modality
        self.stop_time = stop_time
        self.node_name = node_name
        self.received_messages = set()
        self.num_expected_messages = 0
        self.arrived_msgs = 0
        self.all_previous_ids_received = False
        self.node_passing_stats = {}  # Dizionario per tenere traccia delle statistiche di passaggio per ogni nodo
        self.start = rospy.Time.now()
        self.speed = speed
        self.file_name = file_name
        print("FILE NAME = ", file_name)
        
        self.event_sub = rospy.Subscriber(self.node_name, event, self.process_event)
        self.pub_info = rospy.Publisher("/log_info", loginfo, queue_size=20)
        self.log_info_sub = rospy.Subscriber("/log_info", loginfo, self.process_log_info)
        self.type_stats = {}
        self.data_by_type = {}
        self.total_people = 0

    
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
            "num_servers": msg.num_servers,
            "server_time": round(msg.server_time,2),
            "queue_length": msg.queue_array,
            "time_array" : msg.time_array,
            "info": msg.info
            }
            self.total_people += msg.num_servers
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
        # Specifica il percorso della cartella
        folder_path = "/home/ubuntu/Desktop/simulatore/src/simulator/statistic/" + self.file_name
        # Crea la cartella se non esiste già
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        # Specifica il percorso completo del file
        file_path = os.path.join(folder_path, "last_statistic.txt")
        # Crea e scrivi nel file
        with open(file_path, 'w') as file:
            # Reindirizza l'output su 'file'
            sys.stdout = file
            self.print_statistics()
            self.print_data_by_type(False)
            # Ripristina stdout al suo stato originale
            sys.stdout = sys.__stdout__
        
        self.print_statistics()
        self.print_data_by_type(True)
        self.self_kill()

    def print_statistics(self):
        print("################  STATISTIC ############")
        print("\nTempo esecuzione:\t\t",str(round(self.total_seconds,2)), " sec")
        print("Personale usato:\t\t", str(self.total_people))
        print("Events recived:")
        for generator_id in self.get_unique_generator_ids():
            count = sum([1 for gid, _ in self.received_messages if gid == generator_id])
            print(f"\tGenerator {generator_id}:\t\t{count}   messages")

            
        print("\nRoute of events:")
        for msg_type, stats in self.type_stats.items():
            print(f"\tMessage type:\t\t{msg_type}")
            print(f"\tTotal count:\t\t{stats['count']}")
            if stats['count'] > 0:
                total_time = sum([t.to_sec() for t in stats['arrival_times']])
                avg_arrival_time = total_time / stats['count']
                formatted_avg_time = self.format_time(avg_arrival_time)
                print(f"\tAverage arrival time:\t\t{formatted_avg_time}")
                
            passing_stats = self.node_passing_stats.get(msg_type, {})
            total_passing_events = stats['count']
            #print("\nNode passing statistics:")
            for node_id, passing_count in passing_stats.items():
                passing_percentage = (passing_count / total_passing_events) * 100
                print(f"\tNode {node_id}:\t\t{passing_percentage:.2f}%")
                
    def print_data_by_type(self,plot):
        for msg_type, data_list in self.data_by_type.items():
            #print(f"Type {msg_type}:\n")
            print("\nAnalisi code:")
            for data in data_list:
                print(f"\tnome:\t\t{data['node_name']}")
                print(f"\tnumero operatori:\t\t{data['num_servers']} ")
                print(f"\ttempo esecuzione:\t\t{data['server_time']} ")
                print(f"\tutilizzazione totale:\t\t{data['utiliz_tot']}")
                print(f"\tutilizzazione:\t\t{data['utiliz_array']}")
                print(f"\tlunghezza coda:\t\t{data['queue_length']}")
                print(f"\tinfo:\t\t{data['info']}")
                print("\n")
                
                if plot:
                    self.plot_temporal_data(data['queue_length'],data['utiliz_array'],data['time_array'],data['node_name'])
                
    def plot_temporal_data(self,values1, values2,time_array, title):
        time_steps = [(time.to_sec() - self.start.to_sec())*self.speed for time in time_array]
        output_file1 ="/home/ubuntu/Desktop/simulatore/src/simulator/statistic/"
        output_file = output_file1 + file_name + "/" + title + ".png"
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
        plt.savefig(output_file)
        try:
            subprocess.Popen(['xdg-open', output_file])  # Sostituisci 'xdg-open' con il visualizzatore di immagini del tuo sistema
        except FileNotFoundError:
            print("Impossibile aprire il file immagine. Assicurati di avere un visualizzatore di immagini predefinito installato.")
       
        
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

    def self_kill(self): 
        print("Esecuzione terminata")
        # Ottenere il PID del processo corrente (lo script Python in esecuzione)
        current_pid = os.getpid()
        # Simulare l'invio del segnale di interruzione (Ctrl+C) al processo corrente
        os.kill(current_pid, signal.SIGINT)




if __name__ == '__main__':
    rospy.init_node(rospy.get_param("~node_name", "end_node"))
    node_name = rospy.get_param("~node_name", "end_node")
    modality = rospy.get_param("~modality", "events")
    stop_time = rospy.get_param("~stop_time", 540)
    speed = rospy.get_param("~speed", 1)
    file_name = rospy.get_param("~file_name", "no_name")
    print("FILE NAME 1 =", file_name)
    plt.ion()
    
    end_node = EndNode(node_name,modality,stop_time,speed,file_name)
    rospy.spin()
    