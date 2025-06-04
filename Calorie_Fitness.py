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
        valid = True
        
        if not Side_Functions.check_empty(self.target_weight, self.Submit_Button_warning, "⚠ Must Enter A Number"):
            valid = False
        elif int(self.target_weight) < 0:
            valid = False
            self.Submit_Button_warning.configure(text="⚠ Negative Numbers \n aren't allowed.")
        if valid:
            self.Check_if_Sure()
    #I need a function or a method that can store the vars always and use it when needed, Luckily i did find one
    def Insert_Data(self):
        Cur.execute("SELECT Body_Weight, Body_Height, Activity, Age FROM Users WHERE Email = ?", ())
        pass
    
    def Check_if_Sure(self):
        self.Sure_Windows = ctk.CTkToplevel()
        self.Sure_Windows.geometry("400x250")
        self.Sure_Windows.title("Are you sure?")
        ctk.CTkLabel(self.Sure_Windows, text="Are you sure \nyou want to proceed?: ", **Styles.label_styles["subtitle2"]).pack(pady=10)
        ctk.CTkButton(self.Sure_Windows, text="Yes", **Styles.button_styles["Small"], command=lambda: self.Insert_Data()).pack(padx=10, pady=10)
        ctk.CTkButton(self.Sure_Windows, text="No", **Styles.button_styles["Small"], command= self.Sure_Windows.destroy).pack(padx=5, pady=5)
        self.Sure_Windows.attributes("-topmost", True)
    
    def Create_Details_Frame(self):
        bkg_Image = ctk.CTkImage(dark_image=Image.open("Black GYM Background.jpeg"), size=(1000, 700))
        
        bg_label = ctk.CTkLabel(self, image=bkg_Image, text="", fg_color="transparent")
        bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        Title_Label = ctk.CTkLabel(self, text="Give us more information \nso we can serve you better!", 
                                   **Styles.label_styles["subtitle2"])
        Title_Label.place(x=350, y=10)
        
        gender_label = ctk.CTkLabel(self, text="What is your gender?", **Styles.label_styles["Question"])
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
        
        Diet_target_Label = ctk.CTkLabel(self, text="What is your target weight?", **Styles.label_styles["Question"])
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
        Days_off_Cb.set("Cardio with some stretches")
        
        Intensity_Label = ctk.CTkLabel(self, text="Which intensity you will \n find it best for you?: ", **Styles.label_styles["Question"])
        Intensity_Label.place(x=523, y=236)
        
        Intensity_Cb = ctk.CTkComboBox(self, variable=self.intensity_Level, 
                                    values=["Moderate Intensity",
                                            "High Intensity",
                                            "Low Intensity"],
                                    width=307, 
                                    height=52,
                                    **Styles.ComboBox["Box1"])
        Intensity_Cb.place(x=536, y=326)
        Intensity_Cb.set("Moderate Intensity")
        
        Experience_Level_Label = ctk.CTkLabel(self, text="What is your Experience Level?:", **Styles.label_styles["Question"])
        Experience_Level_Label.place(x=476, y=394)
        
        Experience_Level_Cb = ctk.CTkComboBox(self, variable=self.Experience_Level, values=["Standard", "Beginner", "PRO", "Know a bit"],
                                            width=307,
                                            height=52,
                                            **Styles.ComboBox["Box1"])
        Experience_Level_Cb.place(x=536, y=452)
        Experience_Level_Cb.set("Beginner")
        
        Submit_Button = ctk.CTkButton(self, text="SUBMIT", width=238, height=50, 
                                    **Styles.button_styles["Small"], 
                                    command=lambda: self.Submit())
        Submit_Button.place(x=557, y=530)
        
        self.Submit_Button_warning = ctk.CTkLabel(self, text="", **Styles.label_styles["error_title"])
        self.Submit_Button_warning.place(x=826, y=546)
        
        
        