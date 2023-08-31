import os
from tkinter import *
import customtkinter
import imageio
from PIL import Image
import subprocess
import tkinter.filedialog

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"

class Interfaccia(customtkinter.CTk):
    def __init__(self):
        super().__init__()
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
        self.logo_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="nswe")
        
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
        
        button1 = customtkinter.CTkButton(master=tabview.tab("generatore"), text="Add", command=self.add_generator)
        button1.grid(row=10, column=1, padx=(15,5), pady=(5,2),sticky="w")
        
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
        
        button2 = customtkinter.CTkButton(master=tabview.tab("coda"), text="Add", command=self.add_coda)
        button2.grid(row=9, column=1, padx=(15,5), pady=(5,2),sticky="w")
        
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
        self.switch_modality = customtkinter.CTkComboBox(tabview.tab("switch"), values=["split", "type", "attribute", "attribute_split"])
        self.switch_modality.grid(row=3, column=1, padx=(5,15),pady=(5,2),columnspan=2, sticky="we")
        self.t_split_attribute = customtkinter.CTkLabel(tabview.tab("switch"), text="Split Attribute : ", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.t_split_attribute.grid(row=4, column=0, padx=(15,5), pady=(5,2),sticky="w")
        self.split_attribute = customtkinter.CTkEntry(tabview.tab("switch"))
        self.split_attribute.grid(row=4, column=1, padx=(5,15),pady=(5,2),columnspan=2, sticky="we")
        self.t_topic1 = customtkinter.CTkLabel(tabview.tab("switch"), text="Topic1 : ", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.t_topic1.grid(row=5, column=0, padx=(15,5), pady=(5,2),sticky="w")
        self.topic1 = customtkinter.CTkEntry(tabview.tab("switch"))
        self.topic1.grid(row=5, column=1, padx=(5,15),pady=(5,2),columnspan=2, sticky="we")
        self.t_topic2 = customtkinter.CTkLabel(tabview.tab("switch"), text="Topic2 : ", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.t_topic2.grid(row=6, column=0, padx=(15,5), pady=(5,2),sticky="w")
        self.topic2 = customtkinter.CTkEntry(tabview.tab("switch"))
        self.topic2.grid(row=6, column=1, padx=(5,15),pady=(5,2),columnspan=2, sticky="we")
        self.t_attribute_num = customtkinter.CTkLabel(tabview.tab("switch"), text="Numero attributi : ", font=customtkinter.CTkFont(size=12, weight="bold"))
        self.t_attribute_num.grid(row=7, column=0, padx=(15,5), pady=(5,2),sticky="w")
        self.attribute_num = customtkinter.CTkEntry(tabview.tab("switch"))
        self.attribute_num.grid(row=7, column=1, padx=(5,15),pady=(5,2),columnspan=2, sticky="we")

        button_switch = customtkinter.CTkButton(master=tabview.tab("switch"), text="Add", command=self.add_switch)
        button_switch.grid(row=8, column=1, padx=(15,5), pady=(5,2),sticky="w")

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
        
        button_end = customtkinter.CTkButton(master=tabview.tab("end"), text="Add", command=self.add_end)
        button_end.grid(row=10, column=1, padx=(15,5), pady=(5,2),sticky="w")



                
        #file
        self.file_frame = customtkinter.CTkFrame(self)
        self.file_frame.grid(row=0, column=1, padx=(15,5), pady=(5, 5), sticky="nsew",rowspan=2)
        self.textbox = customtkinter.CTkTextbox(master=self.file_frame, width=900,height=650, corner_radius=10)
        self.textbox.grid(row=0, column=0,padx=(35,15), pady=(15, 15), sticky="nsew", columnspan = 3)
        self.textbox.insert("0.0", "<!-- Launch the generator node -->\n<launch>\n")
        self.load_button = customtkinter.CTkButton(master=self.file_frame, text="LOAD", command=self.load_file)
        self.load_button.grid(row=2, column=0, padx=(85,5), pady=(5,2), sticky="w")
        button_save = customtkinter.CTkButton(master=self.file_frame, text="SAVE", command=self.save_file)
        button_save.grid(row=2, column=1, padx=(15,5), pady=(5,2),sticky="w")
        button_run = customtkinter.CTkButton(master=self.file_frame, text="RUN", command=self.run_file)
        button_run.grid(row=2, column=2, padx=(15,5), pady=(5,2),sticky="w")
        
    def add_generator(self):
        print("add_generator")
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
        
    def format_generator_node(self):
        formatted_node = f"""\t<node name="{self.generator_data['node_name']}" pkg="{self.generator_data['pkg']}" type="{self.generator_data['type']}" output="{self.generator_data['output']}">\n"""
        for param, value in self.generator_data['params'].items():
            if value.strip():
                formatted_node += f'\t\t<param name="{param}" value="{value}"/>\n'
        formatted_node += "\t</node>\n\n"
        return formatted_node
      
      
    def add_coda(self):
        self.coda_data = {
            "node_name": self.node_name2.get(),
            "pkg": "simulator",
            "type": "blocco_base.py",
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
    
    def format_coda_node(self):
        formatted_node = f"""\t<node name="{self.coda_data['node_name']}" pkg="{self.coda_data['pkg']}" type="{self.coda_data['type']}" output="{self.coda_data['output']}">\n"""
        for param, value in self.coda_data['params'].items():
            if value.strip():
                formatted_node += f'\t\t<param name="{param}" value="{value}"/>\n'
        formatted_node += "\t</node>\n\n"
        return formatted_node
        
        
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
        
    def format_switch_node(self):
        formatted_node = f"""\t<node name="{self.switch_data['node_name']}" pkg="{self.switch_data['pkg']}" type="{self.switch_data['type']}" output="{self.switch_data['output']}">\n"""
        for param, value in self.switch_data['params'].items():
            if value.strip():
                formatted_node += f'\t\t<param name="{param}" value="{value}"/>\n'
        formatted_node += "\t</node>\n\n"
        return formatted_node

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

    def format_end_node(self):
        formatted_node = f"""\t<node name="{self.end_data['node_name']}" pkg="{self.end_data['pkg']}" type="{self.end_data['type']}" output="{self.end_data['output']}">\n"""
        for param, value in self.end_data['params'].items():
            if value.strip():
                formatted_node += f'\t\t<param name="{param}" value="{value}"/>\n'
        formatted_node += "\t</node>\n\n"
        return formatted_node

    def run_file(self):
        print("Running the script ...")
        self.save_file()  # Salva il file generato
        
        source_command = "source /home/ubuntu/Desktop/simulatore/devel/setup.bash"
        launch_command = "roslaunch simulator generated_launch_file.launch"
        
        full_command = f"{source_command} && {launch_command}"
        
        # Aggiungi 'read -p "Press Enter to exit..."' per mantenere il terminale aperto
        full_command_with_read = f"{full_command} && read -p 'Press Enter to exit...'"
        
        subprocess.Popen(["gnome-terminal", "--", "bash", "-c", f"{full_command_with_read}; exec $SHELL"])

        
        print("Script is running.")
            
    def save_file(self):
        print("saving the script ...")
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

if __name__ == "__main__":
    app = Interfaccia()
    app.mainloop()
