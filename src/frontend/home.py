import tkinter
import tkinter.messagebox
import customtkinter
import pandas as pd
import numpy as np
from pandastable import Table

import test_data

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

data=test_data.data

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Med ARCADE test interface")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=6, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(6, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Med ARCADE", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_home = customtkinter.CTkButton(self.sidebar_frame, command=self.home_button_event, text="Home")
        self.sidebar_button_home.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_priority = customtkinter.CTkButton(self.sidebar_frame, command=self.priority_button_event, text = "Priority")
        self.sidebar_button_priority.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_comments = customtkinter.CTkButton(self.sidebar_frame, command=self.comments_button_event, text = "Comments")
        self.sidebar_button_comments.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_waiting = customtkinter.CTkButton(self.sidebar_frame, command=self.waiting_button_event, text = "Waiting")
        self.sidebar_button_waiting.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_settings = customtkinter.CTkButton(self.sidebar_frame, command=self.settings_button_event, text = "Settings")
        self.sidebar_button_settings.grid(row=5, column=0, padx=20, pady=10)

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 20))

        # create main entry and button
        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter your query...")
        self.entry.grid(row=3, column=1, columnspan=1, padx=(20, 0), pady=(20, 20), sticky="nsew")

        self.search_button = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Search",command=self.search_button_event)
        self.search_button.grid(row=3, column=2, padx=(20, 20), pady=(20, 20), sticky="nsew")
        
       

        # create textbox
        self.data_box = customtkinter.CTkFrame(self, width=250, height=250)
        self.data_box.grid(row=0, column=1, columnspan = 1, padx=(20, 0), pady=(20, 0), sticky="nsew", rowspan=3)
        self.table = pt = Table(self.data_box, dataframe=data)
        pt.show()

        self.option_frame = customtkinter.CTkFrame(self)
        self.option_frame.grid(row=0, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
        
        class_names = np.append(["All"], data['Classification'].unique())
        self.optionmenu_class = customtkinter.CTkOptionMenu(master=self.option_frame, dynamic_resizing=True,
                                                        values=class_names, command=self.change_class_event)
        self.optionmenu_class.grid(row=2, column=2, padx=20, pady=(20, 10))

        task_names = np.append(["All"],data['Tasks'].unique())
        self.optionmenu_task = customtkinter.CTkOptionMenu(master=self.option_frame, dynamic_resizing=True,
                                                        values=task_names, command=self.change_task_event)
        self.optionmenu_task.grid(row=1, column=2, padx=20, pady=(20, 10))
        doc_names = np.append(["All"], data['Doctor'].unique())
        self.optionmenu_doc = customtkinter.CTkOptionMenu(master=self.option_frame, dynamic_resizing=True,
                                                        values=doc_names, command=self.change_doc_event)
        self.optionmenu_doc.grid(row=0, column=2, padx=20, pady=(20, 10))
        

        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        self.optionmenu_class.set("Classification")
        self.optionmenu_task.set("Tasks")
        self.optionmenu_doc.set("Doctor")
       

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def home_button_event(self):
        print("home click")
    
    def priority_button_event(self):
        print("priority click")
    
    def comments_button_event(self):
        print("comments click")
    
    def waiting_button_event(self):
        print("waiting click")

    def settings_button_event(self):
        print("settings click")

    def search_button_event(self):
        print("search click")

    def change_doc_event(self, doc_name: str):
        if doc_name == "All":
            self.table = pt = Table(self.data_box, dataframe=data)
        else:
            temp_data = data[data["Doctor"] == doc_name]
            self.table = pt = Table(self.data_box, dataframe=temp_data)
        pt.show()
        print("change doc to ", doc_name)
    
    def change_task_event(self, task_name: str):
        print("change task to ", task_name)

    def change_class_event(self, class_name: str):
        print("change class to ", class_name)


if __name__ == "__main__":
    app = App()
    app.mainloop()