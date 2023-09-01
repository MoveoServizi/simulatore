import os
from tkinter import *
import customtkinter
import imageio
from PIL import Image
import subprocess
import tkinter.filedialog
import tkinter.simpledialog
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"

class Interfaccia(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.NODE_TYPE_COLORS = {
            "generator": "CornflowerBlue",
            "coda": "IndianRed",
            "switch2": "DarkSeaGreen",
            "end_node": "DarkKhaki" 
            # Aggiungi altri tipi di nodo e colori qui
        }

        self.colors = {}
        self.costruttore_interfaccia()

    def costruttore_interfaccia(self):
        # Configure window
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "Moveo.png")
        
        # Load the image using PIL
        image_data = Image.open(image_path)
        self.logo_image = customtkinter.CTkImage(image_data, size=(160, 90))
        
        self.title("Moveo Servizi - Simulatore flussi")
        self.geometry(f"{1420}x{800}")

        # Configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Create logo widget
        self.logo_frame = customtkinter.CTkFrame(self, fg_color="black")
        self.logo_frame.grid(row=0, column=0, padx=(5, 15), pady=(15, 5), sticky="nsew")
        

        self.logo_label = customtkinter.CTkLabel(self.logo_frame, corner_radius=2, text="", image=self.logo_image)
        self.logo_label.grid(row=0, column=0, padx=(90, 40), pady=(10, 10), sticky="ew")
        
        # create node widget 
        self.node_frame = customtkinter.CTkFrame(self)
        self.node_frame.grid(row=1, column=0, padx=(5,15), pady=(5, 15),rowspan=2, sticky="nsew")
        
        
        tabview = customtkinter.CTkTabview(master=self.node_frame)
        tabview.pack(padx=20, pady=20)

        tabview.add("generatore")  # add tab at the end
        tabview.add("coda")  # add tab at the end
        tabview.add("switch")  # add tab at the end
        tabview.add("end")  # add tab at the end
        tabview.set("generatore")  # set currently visible tab

        ## generatore
        self.t_node_name1 = customtkinter.CTkLabel(tabview.tab("generatore"), text="Nome : ", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.t_node_name1.grid(row=1, column=0, padx=(15,5), pady=(5,2),sticky="w")
        self.node_name1 = customtkinter.CTkEntry(tabview.tab("generatore"))
        self.node_name1.grid(row=1, column=1, padx=(5,15),pady=(5,2),columnspan=2, sticky="we")      
        self.t_node_ID1 = customtkinter.CTkLabel(tabview.tab("generatore"), text="ID : ", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.t_node_ID1.grid(row=2, column=0, padx=(15,5), pady=(5,2),sticky="w")
        self.node_ID1 = customtkinter.CTkEntry(tabview.tab("generatore"))
        self.node_ID1.grid(row=2, column=1, padx=(5,15),pady=(5,2),columnspan=2, sticky="we") 
        self.t_next1 = customtkinter.CTkLabel(tabview.tab("generatore"), text="next : ", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.t_next1.grid(row=3, column=0, padx=(15,5), pady=(5,2),sticky="w")
        self.next1 = customtkinter.CTkEntry(tabview.tab("generatore"))
        self.next1.grid(row=3, column=1, padx=(5,15),pady=(5,2),columnspan=2, sticky="we")
        self.t_num_events = customtkinter.CTkLabel(tabview.tab("generatore"), text="numero eventi : ", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.t_num_events.grid(row=4, column=0, padx=(15,5), pady=(5,2),sticky="w")
        self.num_events = customtkinter.CTkEntry(tabview.tab("generatore"))
        self.num_events.grid(row=4, column=1, padx=(5,15),pady=(5,2),columnspan=2, sticky="we")
        self.t_frequenza = customtkinter.CTkLabel(tabview.tab("generatore"), text="frequenza : ", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.t_frequenza.grid(row=5, column=0, padx=(15,5), pady=(5,2),sticky="w")
        self.frequenza = customtkinter.CTkEntry(tabview.tab("generatore"))
        self.frequenza.grid(row=5, column=1, padx=(5,15),pady=(5,2),columnspan=2, sticky="we")
        self.t_event_type = customtkinter.CTkLabel(tabview.tab("generatore"), text="event type : ", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.t_event_type.grid(row=6, column=0, padx=(15,5), pady=(5,2),sticky="w")
        self.event_type = customtkinter.CTkEntry(tabview.tab("generatore"))
        self.event_type.grid(row=6, column=1, padx=(5,15),pady=(5,2),columnspan=2, sticky="we")
        self.t_attribute1 = customtkinter.CTkLabel(tabview.tab("generatore"), text="attribute1 : ", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.t_attribute1.grid(row=7, column=0, padx=(15,5), pady=(5,2),sticky="w")
        self.attribute1 = customtkinter.CTkEntry(tabview.tab("generatore"))
        self.attribute1.grid(row=7, column=1, padx=(5,15),pady=(5,2),columnspan=2, sticky="we")
        self.t_value1 = customtkinter.CTkLabel(tabview.tab("generatore"), text="value1 : ", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.t_value1.grid(row=8, column=0, padx=(15,5), pady=(5,2),sticky="w")
        self.value1 = customtkinter.CTkEntry(tabview.tab("generatore"))
        self.value1.grid(row=8, column=1, padx=(5,15),pady=(5,2),columnspan=2, sticky="we")
        
        reset1 = customtkinter.CTkButton(master=tabview.tab("generatore"), text="Reset", command=self.reset_generator)
        reset1.grid(row=10, column=0, padx=(15,5), pady=(20,10),sticky="w")
        button1 = customtkinter.CTkButton(master=tabview.tab("generatore"), text="Add", command=self.add_generator)
        button1.grid(row=10, column=1, padx=(15,5), pady=(20,10),sticky="w")
        
        ## coda
        self.t_node_name2 = customtkinter.CTkLabel(tabview.tab("coda"), text="Nome : ", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.t_node_name2.grid(row=1, column=0, padx=(15,5), pady=(5,2),sticky="w")
        self.node_name2 = customtkinter.CTkEntry(tabview.tab("coda"))
        self.node_name2.grid(row=1, column=1, padx=(5,15),pady=(5,2),columnspan=2, sticky="we")
        self.t_node_ID2 = customtkinter.CTkLabel(tabview.tab("coda"), text="ID : ", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.t_node_ID2.grid(row=2, column=0, padx=(15,5), pady=(5,2),sticky="w")
        self.node_ID2 = customtkinter.CTkEntry(tabview.tab("coda"))
        self.node_ID2.grid(row=2, column=1, padx=(5,15),pady=(5,2),columnspan=2, sticky="we")
        self.t_next2 = customtkinter.CTkLabel(tabview.tab("coda"), text="next : ", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.t_next2.grid(row=3, column=0, padx=(15,5), pady=(5,2),sticky="w")
        self.next2 = customtkinter.CTkEntry(tabview.tab("coda"))
        self.next2.grid(row=3, column=1, padx=(5,15),pady=(5,2),columnspan=2, sticky="we")
        self.t_num_servers = customtkinter.CTkLabel(tabview.tab("coda"), text="numero server : ", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.t_num_servers.grid(row=4, column=0, padx=(15,5), pady=(5,2),sticky="w")
        self.num_servers = customtkinter.CTkEntry(tabview.tab("coda"))
        self.num_servers.grid(row=4, column=1, padx=(5,15),pady=(5,2),columnspan=2, sticky="we")
        self.t_server_time = customtkinter.CTkLabel(tabview.tab("coda"), text="tempo server : ", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.t_server_time.grid(row=5, column=0, padx=(15,5), pady=(5,2),sticky="w")
        self.server_time = customtkinter.CTkEntry(tabview.tab("coda"))
        self.server_time.grid(row=5, column=1, padx=(5,15),pady=(5,2),columnspan=2, sticky="we")
        
        reset2 = customtkinter.CTkButton(master=tabview.tab("coda"), text="Reset", command=self.reset_coda)
        reset2.grid(row=10, column=0, padx=(15,5), pady=(20,10),sticky="w")
        button2 = customtkinter.CTkButton(master=tabview.tab("coda"), text="Add", command=self.add_coda)
        button2.grid(row=10, column=1, padx=(15,5), pady=(20,10),sticky="w")
        
        ## switch
        self.t_node_name3 = customtkinter.CTkLabel(tabview.tab("switch"), text="Nome : ", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.t_node_name3.grid(row=1, column=0, padx=(15,5), pady=(5,2),sticky="w")
        self.node_name3 = customtkinter.CTkEntry(tabview.tab("switch"))
        self.node_name3.grid(row=1, column=1, padx=(5,15),pady=(5,2),columnspan=2, sticky="we")
        self.t_node_ID3 = customtkinter.CTkLabel(tabview.tab("switch"), text="ID : ", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.t_node_ID3.grid(row=2, column=0, padx=(15,5), pady=(5,2),sticky="w")
        self.node_ID3 = customtkinter.CTkEntry(tabview.tab("switch"))
        self.node_ID3.grid(row=2, column=1, padx=(5,15),pady=(5,2),columnspan=2, sticky="we")
        self.t_switch_modality = customtkinter.CTkLabel(tabview.tab("switch"), text="Modalità : ", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.t_switch_modality.grid(row=3, column=0, padx=(15,5), pady=(5,2),sticky="w")
        self.switch_modality = customtkinter.CTkComboBox(tabview.tab("switch"), values=["split", "type", "attribute", "split_attribute"])
        self.switch_modality.grid(row=3, column=1, padx=(5,15),pady=(5,2),columnspan=2, sticky="we")
        self.t_attribute_num = customtkinter.CTkLabel(tabview.tab("switch"), text="Numero attributi : ", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.t_attribute_num.grid(row=4, column=0, padx=(15,5), pady=(5,2),sticky="w")
        self.attribute_num = customtkinter.CTkEntry(tabview.tab("switch"))
        self.attribute_num.grid(row=4, column=1, padx=(5,15),pady=(5,2),columnspan=2, sticky="we")
        self.t_split_attribute = customtkinter.CTkLabel(tabview.tab("switch"), text="Split Attribute : ", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.t_split_attribute.grid(row=5, column=0, padx=(15,5), pady=(5,2),sticky="w")
        self.split_attribute = customtkinter.CTkEntry(tabview.tab("switch"))
        self.split_attribute.grid(row=5, column=1, padx=(5,15),pady=(5,2),columnspan=2, sticky="we")
        self.t_topic1 = customtkinter.CTkLabel(tabview.tab("switch"), text="Topic1 : ", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.t_topic1.grid(row=6, column=0, padx=(15,5), pady=(5,2),sticky="w")
        self.topic1 = customtkinter.CTkEntry(tabview.tab("switch"))
        self.topic1.grid(row=6, column=1, padx=(5,15),pady=(5,2),columnspan=2, sticky="we")
        self.t_topic2 = customtkinter.CTkLabel(tabview.tab("switch"), text="Topic2 : ", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.t_topic2.grid(row=7, column=0, padx=(15,5), pady=(5,2),sticky="w")
        self.topic2 = customtkinter.CTkEntry(tabview.tab("switch"))
        self.topic2.grid(row=7, column=1, padx=(5,15),pady=(5,2),columnspan=2, sticky="we")
        
        reset3 = customtkinter.CTkButton(master=tabview.tab("switch"), text="Reset", command=self.reset_switch)
        reset3.grid(row=10, column=0, padx=(15,5), pady=(20,10),sticky="w")
        button_switch = customtkinter.CTkButton(master=tabview.tab("switch"), text="Add", command=self.add_switch)
        button_switch.grid(row=10, column=1, padx=(15,5), pady=(20,10),sticky="w")

        #end_node
        self.t_node_name4 = customtkinter.CTkLabel(tabview.tab("end"), text="Nome : ", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.t_node_name4.grid(row=1, column=0, padx=(15,5), pady=(5,2),sticky="w")
        self.node_name4 = customtkinter.CTkEntry(tabview.tab("end"))
        self.node_name4.grid(row=1, column=1, padx=(5,15),pady=(5,2),columnspan=2, sticky="we")
        self.t_node_ID4 = customtkinter.CTkLabel(tabview.tab("end"), text="ID : ", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.t_node_ID4.grid(row=2, column=0, padx=(15,5), pady=(5,2),sticky="w")
        self.node_ID4 = customtkinter.CTkEntry(tabview.tab("end"))
        self.node_ID4.grid(row=2, column=1, padx=(5,15),pady=(5,2),columnspan=2, sticky="we")
        
        self.t_end_modality = customtkinter.CTkLabel(tabview.tab("end"), text="Modalità : ", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.t_end_modality.grid(row=3, column=0, padx=(15,5), pady=(5,2),sticky="w")
        self.end_modality = customtkinter.CTkComboBox(tabview.tab("end"), values=["events", "time"])
        self.end_modality.grid(row=3, column=1, padx=(5,15),pady=(5,2),columnspan=2, sticky="we")
        self.t_stop_time = customtkinter.CTkLabel(tabview.tab("end"), text="Tempo di arresto : ", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.t_stop_time.grid(row=4, column=0, padx=(15,5), pady=(5,2),sticky="w")
        self.stop_time = customtkinter.CTkEntry(tabview.tab("end"))
        self.stop_time.grid(row=4, column=1, padx=(5,15),pady=(5,2),columnspan=2, sticky="we")
        
        reset4 = customtkinter.CTkButton(master=tabview.tab("end"), text="Reset", command=self.reset_end_node)
        reset4.grid(row=10, column=0, padx=(15,5), pady=(20,10),sticky="w")
        button_end = customtkinter.CTkButton(master=tabview.tab("end"), text="Add", command=self.add_end)
        button_end.grid(row=10, column=1, padx=(15,5), pady=(20,10),sticky="w")



                
        ### file tab ##
        self.file_frame = customtkinter.CTkFrame(self)
        self.file_frame.grid(row=0, column=1, padx=(5,15), pady=(5, 5), sticky="nsew",rowspan=2)
        self.tabview_main = customtkinter.CTkTabview(master=self.file_frame)
        self.tabview_main.grid(row=0, column=1, padx=(15,15), pady=(15, 20), sticky="nsew")
        
        
        self.tabview_main.add("launch_file") 
        self.tabview_main.add("grafo") 

       # Visualizzazione grafo
        self.fig, self.ax = plt.subplots(figsize=(9.5,6.5))
        canvas = FigureCanvasTkAgg(self.fig, master=self.tabview_main.tab("grafo"))
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=0, column=0, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.G = nx.Graph()
        button_grafo = customtkinter.CTkButton(self.tabview_main.tab("grafo"), text="Visualizza grafo", command=self.visualizza_grafo)
        button_grafo.grid(row=2, column=0, padx=(15,5), pady=(5,2),sticky="w") 
        
        ## generazione launch file
        self.textbox = customtkinter.CTkTextbox(self.tabview_main.tab("launch_file") , width=900,height=650, corner_radius=10)
        self.textbox.grid(row=0, column=0,padx=(35,15), pady=(15, 15), sticky="nsew", columnspan = 3)
        self.textbox.insert("0.0", "<!-- Create the launch file for ROS -->\n<launch>\n")
        self.load_button = customtkinter.CTkButton(self.tabview_main.tab("launch_file"), text="LOAD", command=self.load_file)
        self.load_button.grid(row=2, column=0, padx=(85,5), pady=(5,2), sticky="w")
        button_save = customtkinter.CTkButton(self.tabview_main.tab("launch_file"), text="SAVE", command=lambda: self.save_file(True))
        button_save.grid(row=2, column=1, padx=(15,5), pady=(5,2),sticky="w")
        button_run = customtkinter.CTkButton(self.tabview_main.tab("launch_file"), text="RUN", command=self.run_file)
        button_run.grid(row=2, column=2, padx=(15,5), pady=(5,2),sticky="w")
    
    
    ## funzioni pannello generatore  
    def add_generator(self):
        self.generator_data = {
            "node_name": self.node_name1.get(),
            "pkg": "simulator",
            "type": "generator.py",
            "output": "screen",
            "params": {
                "node_id": self.node_ID1.get(),
                "node_name": self.node_name1.get(),
                "next_element": self.next1.get(),
                "gen_freq": self.frequenza.get(),
                "num_messages": self.num_events.get(),
                "event_type": self.event_type.get(),
                "attribute1": self.attribute1.get(),
                "value1": self.value1.get(),
            }
        }
        generator_node_text = self.format_generator_node()
        self.textbox.insert("end", generator_node_text)
        
        # Aggiungi i nodi e le connessioni al grafo
        self.G.add_node(self.node_name1.get())
        self.colors[self.node_name1.get()] = self.NODE_TYPE_COLORS.get("generator")
        if self.next1.get() not in self.G:
            self.colors[self.next1.get()] = "LightGray"
        self.G.add_edge(self.node_name1.get(), self.next1.get())
        self.visualizza_grafo()
        
    def format_generator_node(self):
        formatted_node = f"""\t<node name="{self.generator_data['node_name']}" pkg="{self.generator_data['pkg']}" type="{self.generator_data['type']}" output="{self.generator_data['output']}">\n"""
        for param, value in self.generator_data['params'].items():
            if value.strip():
                formatted_node += f'\t\t<param name="{param}" value="{value}"/>\n'
        formatted_node += "\t</node>\n\n"
        return formatted_node
    
    def reset_generator(self):
        self.node_name1.delete(0,END)
        self.node_ID1.delete(0,END)
        self.next1.delete(0,END)
        self.num_events.delete(0,END)
        self.frequenza.delete(0,END)
        self.event_type.delete(0,END)
        self.attribute1.delete(0,END)
        self.value1.delete(0,END)
          
    ## funzioni pannello coda 
    def add_coda(self):
        self.coda_data = {
            "node_name": self.node_name2.get(),
            "pkg": "simulator",
            "type": "coda.py",
            "output": "screen",
            "params": {
                "node_id": self.node_ID2.get(),
                "node_name": self.node_name2.get(),
                "next_element": self.next2.get(),
                "num_servers": self.num_servers.get(),
                "server_time": self.server_time.get(),
            }
        }
        coda_node_text = self.format_coda_node()
        self.textbox.insert("end", coda_node_text)
        # Aggiungi i nodi e le connessioni al grafo
        self.G.add_node(self.node_name2.get())
        self.colors[self.node_name2.get()] = self.NODE_TYPE_COLORS.get("coda")
        if self.next2.get() not in self.G:
            self.colors[self.next2.get()] = "LightGray"
        self.G.add_edge(self.node_name2.get(), self.next2.get())
        self.visualizza_grafo()
    
    def format_coda_node(self):
        formatted_node = f"""\t<node name="{self.coda_data['node_name']}" pkg="{self.coda_data['pkg']}" type="{self.coda_data['type']}" output="{self.coda_data['output']}">\n"""
        for param, value in self.coda_data['params'].items():
            if value.strip():
                formatted_node += f'\t\t<param name="{param}" value="{value}"/>\n'
        formatted_node += "\t</node>\n\n"
        return formatted_node
      
    def reset_coda(self):
        self.node_name2.delete(0,END)
        self.node_ID2.delete(0,END)
        self.next2.delete(0,END)
        self.num_servers.delete(0,END)
        self.server_time.delete(0,END)  
    
    ## funzionni pannello switch  
    def add_switch(self):
        self.switch_data = {
            "node_name": self.node_name3.get(),
            "pkg": "simulator",
            "type": "switch2.py",
            "output": "screen",
            "params": {
                "node_id": self.node_ID3.get(),
                "node_name": self.node_name3.get(),
                "modality": self.switch_modality.get(),
                "split_attribute": self.split_attribute.get(),
                "topic1": self.topic1.get(),
                "topic2": self.topic2.get(),
                "attribute_num": self.attribute_num.get(),
                # Aggiungi altri campi...
            }
        }
        switch_node_text = self.format_switch_node()
        self.textbox.insert("end", switch_node_text)
        # Aggiungi i nodi e le connessioni al grafo
        self.G.add_node(self.node_name3.get())
        self.colors[self.node_name3.get()] =  self.NODE_TYPE_COLORS.get("switch2")
        if self.topic1.get() not in self.G:
            self.colors[self.topic1.get()] = "LightGray"
        if self.topic2.get() not in self.G:
            self.colors[self.topic2.get()] = "LightGray"
        self.G.add_edge(self.node_name3.get(), self.topic1.get())
        self.G.add_edge(self.node_name3.get(), self.topic2.get())
        self.visualizza_grafo()
        
    def format_switch_node(self):
        formatted_node = f"""\t<node name="{self.switch_data['node_name']}" pkg="{self.switch_data['pkg']}" type="{self.switch_data['type']}" output="{self.switch_data['output']}">\n"""
        for param, value in self.switch_data['params'].items():
            if value.strip():
                formatted_node += f'\t\t<param name="{param}" value="{value}"/>\n'
        formatted_node += "\t</node>\n\n"
        return formatted_node

    def reset_switch(self):
        self.node_ID3.delete(0,END)
        self.node_name3.delete(0,END)
        self.switch_modality.set("split")
        self.attribute_num.delete(0,END)
        self.split_attribute.delete(0,END)
        self.topic1.delete(0,END)
        self.topic2.delete(0,END)

    ## pannello funzioni end_node
    def add_end(self):
        self.end_data = {
            "node_name": self.node_name4.get(),
            "pkg": "simulator",
            "type": "end_node.py",
            "output": "screen",
            "params": {
                "node_id": self.node_ID4.get(),
                "node_name": self.node_name4.get(),
                "modality": self.end_modality.get(),
                "stop_time": self.stop_time.get(),
            }
        }
        end_node_text = self.format_end_node()
        self.textbox.insert("end", end_node_text)
        self.textbox.insert("end", "</launch>\n")
        # Aggiungi i nodi e le connessioni al grafo
        self.G.add_node(self.node_name4.get())
        self.colors[self.node_name4.get()] =  self.NODE_TYPE_COLORS.get("end_node")
        self.visualizza_grafo()

    def format_end_node(self):
        formatted_node = f"""\t<node name="{self.end_data['node_name']}" pkg="{self.end_data['pkg']}" type="{self.end_data['type']}" output="{self.end_data['output']}">\n"""
        for param, value in self.end_data['params'].items():
            if value.strip():
                formatted_node += f'\t\t<param name="{param}" value="{value}"/>\n'
        formatted_node += "\t</node>\n\n"
        return formatted_node

    def reset_end_node(self):
        self.node_name4.delete(0,END)
        self.node_ID4.delete(0,END)
        self.end_modality.set("events")
        self.stop_time.delete(0,END)
        
    ## file menagment   
    def run_file(self):
        print("Running the script ...")
        self.save_file(False)  # Salva il file generato
        
        source_command = "source devel/setup.bash" #/home/ubuntu/Desktop/simulatore/
        launch_command = "roslaunch simulator generated_launch_file.launch"
        
        full_command = f"{source_command} && {launch_command}"
        
        # Aggiungi 'read -p "Press Enter to exit..."' per mantenere il terminale aperto
        full_command_with_read = f"{full_command} && read -p 'Press Enter to exit...'"
        
        graph = "rqt_graph"
        
        subprocess.Popen(["gnome-terminal", "--", "bash", "-c", f"{full_command_with_read}; exec $SHELL"])
        subprocess.Popen(["gnome-terminal", "--", "bash", "-c", f"{graph}; exec $SHELL"])
        
        print("Script is running.")
            
    def save_file(self,popup):
        print("saving the script ...")
        # Mostra un popup per inserire il nome del file
        if popup:
            file_name = tkinter.simpledialog.askstring("Salva File", "Inserisci il nome del file:", initialvalue="")
            if file_name:
                file_path = "src/simulator/launch/" + file_name + ".launch"  # Aggiunge l'estensione .launch al nome del file
                
        else:
            file_path = "src/simulator/launch/generated_launch_file.launch"  # Scegli il percorso e il nome del file di destinazione
        launch_text = self.textbox.get("1.0", "end")  # Ottieni il testo completo dal textbox
                
        with open(file_path, "w") as file:
            file.write(launch_text)
            
        print("File saved:", file_path)
        
    def load_file(self):
        file_path = tkinter.filedialog.askopenfilename(filetypes=[("Launch files", "*.launch")])
        if file_path:
            with open(file_path, "r") as file:
                launch_text = file.read()
                self.textbox.delete("1.0", "end")
                self.textbox.insert("1.0", launch_text)
            print("File loaded:", file_path)
            self.read_textbox()
            self.visualizza_grafo()
    
    ## tab grafico
    def visualizza_grafo(self):

        # Visualizza il grafo
        self.ax.clear()
        
        pos = nx.spring_layout(self.G)  # Imposta il layout del grafo
        labels = {node: node for node in self.G.nodes()}  # Usa le etichette dei nodi
        # Ottieni i colori dei nodi dalla lista dei colori associati ai nomi dei nodi
        node_colors = [self.colors[nodo] for nodo in self.G.nodes()]
        # Disegna il grafo con i colori specifici dei nodi
        nx.draw(self.G, pos, with_labels=True, labels=labels, node_size=1500, node_color=node_colors, font_size=10, ax=self.ax)
        self.ax.set_facecolor('black')
        # Disegna il grafo aggiornato
        self.fig.canvas.draw()
        
    
    def read_textbox(self):
        launch_text = self.textbox.get("1.0", "end")       
        self.G.clear()
        lines = launch_text.splitlines()
        current_node_name = None # Variabile per tenere traccia del nome del nodo corrente
        for line in lines:
            line = line.strip().lower() # Rimuovi spazi iniziali e finali e converti in minuscolo per una migliore corrispondenza
            # Verifica se questa riga contiene un nuovo nodo
            if line.startswith("<node"):
                
                [node_name, node_type] = self.extract_node_name(line) # Estrai il nome del nodo
                print(node_name, node_type)
                if node_name:
                    current_node_name = node_name
                    # Aggiungi il nodo al grafo
                    self.G.add_node(node_name)
                    self.colors[node_name]=self.NODE_TYPE_COLORS.get(node_type, "skyblue")     
            elif line.startswith("</node>"):
                current_node_name = None
            elif current_node_name:
                # Verifica se questa riga contiene un parametro del nodo
                self.extract_connection(line, node_name,node_type)


    def extract_node_name(self, line):
        name = ""
        type = ""
        start = line.find('name="')
        start_type = line.find('type="')
        if start != -1:
            start += len('name="')
            end = line.find('"', start)
            if end != -1:
                name = line[start:end]
        if start_type != -1:
            start_type += len('type="')
            end_type = line.find('.', start)
            if end_type != -1:
                type = line[start_type:end_type]
        
        return name, type

    def extract_connection(self, line,node_name, node_type):
        if node_type == "switch2":
            start_name1 = line.find('"topic1" value="')
            start_name2 = line.find('"topic2" value="')
            if start_name1 != -1:
                start_name1 += len('"topic1" value="')
                end_name = line.find('"', start_name1)
                next_node = line[start_name1:end_name]
                self.G.add_edge(node_name, next_node)
            if start_name2 != -1:
                start_name2 += len('"topic2" value="')
                end_name = line.find('"', start_name2)
                next_node = line[start_name2:end_name]
                self.G.add_edge(node_name, next_node)  
        else:
            start_name = line.find('"next_element" value="')
            if start_name != -1:
                start_name += len('"next_element" value="')
                end_name = line.find('"', start_name)
                next_node = line[start_name:end_name]
                self.G.add_edge(node_name, next_node)



if __name__ == "__main__":
    app = Interfaccia()
    app.mainloop()
