import os
from tkinter import *
import customtkinter
import imageio
from PIL import Image

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
        
        button = customtkinter.CTkButton(master=tabview.tab("generatore"), text="Add", command=self.add_generator)
        button.grid(row=10, column=1, padx=(15,5), pady=(5,2),sticky="w")
        
        #file
        self.file_frame = customtkinter.CTkFrame(self)
        self.file_frame.grid(row=0, column=1, padx=(15,5), pady=(5, 5), sticky="nsew",rowspan=2)
        self.textbox = customtkinter.CTkTextbox(master=self.file_frame, width=900,height=750, corner_radius=10)
        self.textbox.grid(row=0, column=0,padx=(15,15), pady=(15, 15), sticky="nsew")
        self.textbox.insert("0.0", "<!-- Launch the generator node -->\n<launch>\n")
        
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
            formatted_node += f'\t\t<param name="{param}" value="{value}"/>\n'
        formatted_node += "\t</node>\n\n"
        return formatted_node
        
        
if __name__ == "__main__":
    app = Interfaccia()
    app.mainloop()
