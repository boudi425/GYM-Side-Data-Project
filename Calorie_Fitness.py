import customtkinter as ctk
import sqlite3
import Styles
import Side_Functions
import os
import math

#Starting the part 2 from the project 
Con = sqlite3.connect("Users_Data.db")
Cur = Con.cursor()
with open("GYM&User_DATA.sql", "r") as Table_Query:
    Cur.executescript(Table_Query.read())

class Program_setUp(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.Diet_Goal = ctk.StringVar()
        self.target_weight = ctk.IntVar()
        self.gender = ctk.StringVar()
        self.Training_Days_Ava = ctk.StringVar()
        self.intensity_Level = ctk.StringVar()
        self.Days_Off_Activity = ctk.StringVar()
        self.Experience_Level = ctk.StringVar()
        self.Create_Details_Frame()
        
    def Submit(self):
        pass
    
    def Insert_Data(self):
        pass
    
    def Check_if_Sure(self):
        pass
    
    def Create_Details_Frame(self):
        Title_Label = ctk.CTkLabel(self, text="Give us more information \nso we can serve you better!", **Styles.label_styles["subtitle2"])
        Title_Label.place(x=240, y=10)
        
        Diet_Goal_Label = ctk.CTkLabel(self, text="What is your Diet Goal?", **Styles.label_styles["title2"])
        Diet_Goal_Label.place(x=168, y=68)
        
        Diet_Goal_Cb = ctk.CTkComboBox(self, values=["Maintain My Weight",
                                                    "Gain Weight",
                                                    "Lose Weight"],
                                            width=425,
                                            height=70,
                                            variable=self.Diet_Goal,
                                            state="readonly",
                                            border_color="#4A90E2",
                                            bg_color="#2B2B2B",
                                            dropdown_fg_color="#2B2B2B",
                                            dropdown_text_color="white",
                                            text_color="white",
                                            button_color="grey",
                                            font=("Lato", 35, "bold"),
                                            dropdown_font=("Lato", 35, "bold"))
        Diet_Goal_Cb.place(x=187, y=138)
        Diet_Goal_Cb.set("Maintain My Weight")
        
        Diet_target_Label = ctk.CTkLabel(self, text="What is your target weight", **Styles.label_styles["subtitle2"])
        Diet_target_Label.place(x=140, y=230)
        
        Diet_Target_Entry = ctk.CTkEntry(self, textvariable=self.target_weight, **Styles.entry_styles["default"], width=140, height=70)
        Diet_Target_Entry.place(x=322, y=290)
        
        gender_label = ctk.CTkLabel(self, text="What is your gender", **Styles.label_styles["subtitle2"])
        gender_label.place(x=199, y=365)
        
        gender_cb = ctk.CTkComboBox(self, variable=self.gender, values=["Male", "Female"], 
                                            width=140,
                                            height=70,
                                            state="readonly",
                                            border_color="#4A90E2",
                                            bg_color="#2B2B2B",
                                            dropdown_fg_color="#2B2B2B",
                                            dropdown_text_color="white",
                                            text_color="white",
                                            button_color="grey",
                                            font=("Lato", 20, "bold"),
                                            dropdown_font=("Lato", 20, "bold"))
        gender_cb.place(x=322, y=420)
        gender_cb.set("Male")