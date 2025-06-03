import customtkinter as ctk
import sqlite3
import Styles
import Side_Functions
import os
import math
from PIL import Image
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
        bkg_Image = ctk.CTkImage(dark_image=Image.open("GYM_Background.jpeg"), size=(1000, 700))
        
        bg_label = ctk.CTkLabel(self, image=bkg_Image, text="", fg_color="transparent")
        bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        Title_Label = ctk.CTkLabel(self, text="Give us more information \nso we can serve you better!", 
                                   **Styles.label_styles["subtitle2"])
        Title_Label.place(x=350, y=10)
        
        gender_label = ctk.CTkLabel(self, text="What is your gender", **Styles.label_styles["Question"])
        gender_label.place(x=80, y=89)
        
        gender_cb = ctk.CTkComboBox(self, variable=self.gender, values=["Male", "Female"], 
                                            width=160,
                                            height=50,
                                            state="readonly",
                                            border_color="#4A90E2",
                                            bg_color="#2B2B2B",
                                            dropdown_fg_color="#2B2B2B",
                                            dropdown_text_color="white",
                                            text_color="white",
                                            button_color="grey",
                                            font=("Lato", 20, "bold"),
                                            dropdown_font=("Lato", 20, "bold"))
        gender_cb.place(x=160, y=154)
        gender_cb.set("Male")
        
        
        Diet_Goal_Label = ctk.CTkLabel(self, text="What is your Diet Goal?", **Styles.label_styles["Question"])
        Diet_Goal_Label.place(x=79, y=231)
        
        Diet_Goal_Cb = ctk.CTkComboBox(self, values=["Maintain My Weight",
                                                    "Gain Weight",
                                                    "Lose Weight"],
                                            width=307,
                                            height=52,
                                            variable=self.Diet_Goal,
                                            state="readonly",
                                            border_color="#4A90E2",
                                            bg_color="#2B2B2B",
                                            dropdown_fg_color="#2B2B2B",
                                            dropdown_text_color="white",
                                            text_color="white",
                                            button_color="grey",
                                            font=("Lato", 25, "bold"),
                                            dropdown_font=("Lato", 25, "bold"))
        Diet_Goal_Cb.place(x=92, y=289)
        Diet_Goal_Cb.set("Maintain My Weight")
        
        Diet_target_Label = ctk.CTkLabel(self, text="What is your target weight", **Styles.label_styles["Question"])
        Diet_target_Label.place(x=50, y=360)
        
        Diet_Target_Entry = ctk.CTkEntry(self, textvariable=self.target_weight, **Styles.entry_styles["default"], 
                                        width=128, height=50)
        Diet_Target_Entry.place(x=182, y=410)
        
        Training_Days_Label = ctk.CTkLabel(self, text="How Many Days can you train?: ", **Styles.label_styles["Question"])
        Training_Days_Label.place(x=31, y=481)
        
        Training_Days_Cb = ctk.CTkComboBox(self, variable=self.Training_Days_Ava, values=["3 Days With intense or moderate exercises",
                                                                                        "4-6 Days with intense or moderate exercises",
                                                                                        "Full Week With intense or moderate exercises"],
                                        **Styles.ComboBox["Box1"],
                                        width=470,
                                        height=37)
        Training_Days_Cb.place(x=31, y=539)
        Training_Days_Cb.set("4-6 Days with intense or moderate exercises")
        
        Days_off_Label = ctk.CTkLabel(self, text="On Days you don't work \nHow Active are you?", **Styles.label_styles["Question"])
        Days_off_Label.place(x=511, y=80)
        
        Days_off_Cb = ctk.CTkComboBox(self, variable=self.Days_Off_Activity, values=["Moderate exercises with normal movement",
                                                                                    "No Moving at all",
                                                                                    "Don't Take rest Days",
                                                                                    "Cardio with some stretches",]
                                                                                    ,**Styles.ComboBox["Box1"],
                                                                                    width=307,
                                                                                    height=52)
        Days_off_Cb.place(x=541, y=171)
        