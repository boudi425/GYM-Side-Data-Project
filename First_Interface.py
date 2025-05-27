import customtkinter as ctk
import Styles
import datetime
import sqlite3
import Side_Functions
import Web_Scrapping
import os
import json
import sys

#This will be the Main Interface (start up interface you can say also)
#I will Start with the basics
#Zero basic Set up
Con = sqlite3.connect("Users_Data.db")
Cur = Con.cursor()
with open("GYM&User_DATA.sql", "r") as Table_Query:
    Cur.executescript(Table_Query.read())
#First: Sign up Interface/Class

# // Main Window...
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
ctk.set_window_scaling(1)
ctk.set_widget_scaling(1)

class Sign_Up(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.username = ctk.StringVar()
        self.password = ctk.StringVar()
        self.email = ctk.StringVar()
        self.body_Weight = ctk.IntVar(value=0)
        self.body_Height = ctk.IntVar(value=0)
        self.age = ctk.IntVar(value=0)
        self.Activity = ctk.StringVar(value="Moderate: exercise 4-5 times/week")
        self.Status = False
        self.Create_Sign_Up_Frame()
        
    def Error_Popup_Window(self, Label_Text, Button_Text):
        root = ctk.CTkToplevel()
        root.geometry("250x150")
        root.title("Error")
        ctk.CTkLabel(root, text=Label_Text, **Styles.label_styles["subtitle2"])
        ctk.CTkButton(root, text=Button_Text, **Styles.button_styles["Small"], command=root.destroy)
    def check_empty(self, entry, warning_label, message):
        if isinstance(entry.get(), str):
            if entry.get().strip() == "":
                warning_label.configure(text=message)
                return False
            else:
                warning_label.configure(text="")
                return True
        if isinstance(entry.get(), int):
            if entry.get() == 0:
                warning_label.configure(text=message)
                return False
            else:
                warning_label.configure(text="")
                return True


    def Submit(self):
        valid = True
        
        if not self.check_empty(self.username, self.username_warning, "⚠ Username required"):
            valid = False
        if not self.check_empty(self.password, self.password_warning, "⚠ Password required"):
            valid = False
        if not self.check_empty(self.body_Weight, self.weight_warning, "⚠ Weight required"):
            valid = False
        if not self.check_empty(self.body_Height, self.height_warning, "⚠ Height required"):
            valid = False
        if not self.check_empty(self.email, self.email_warning, "⚠ Email required"):
            valid = False
        if not self.check_empty(self.age, self.age_warning, "⚠ Age required"):
            valid = False
        
        if valid:
            self.SignUp_Data_Management()

    def SignUp_Data_Management(self):
        Cur.execute("""INSERT INTO Users(
                    Name, 
                    Password, 
                    Email, 
                    Body_Weight, 
                    Body_Height, 
                    Activity, 
                    Age, 
                    Status) VALUES(?, ?, ?, ?, ?, ?, ?, ?)
                    """, (self.username.get(), self.password.get(), self.email.get()
                        , self.body_Weight.get(), self.body_Height.get(),
                        self.age.get(), self.Activity.get(), self.Status))
        Con.commit()
    
    def Create_Sign_Up_Frame(self):
        Title_Label = ctk.CTkLabel(self, 
                                text="Sign Up To Experience All Our WORK!",
                                **Styles.label_styles["title2"])
        Title_Label.place(relx=0.5, rely=0.05, anchor="center")
        
        User_Name_Label = ctk.CTkLabel(self,
                                    text="Username:",
                                    width=245,
                                    height=58,
                                    **Styles.label_styles["title2"])
        User_Name_Label.place(x=405, y=72)
        self.username = ctk.CTkEntry(self,
                                    width=346,
                                    height=50,
                                    **Styles.entry_styles["default"])
        self.username.place(x=405, y=134)
        
        self.username_warning = ctk.CTkLabel(self, text="", width=140, height=24, **Styles.label_styles["error_title"])
        self.username_warning.place(x=405, rely=198)
#-------------------------------------------------------------------------------------------------------
        Email_Label = ctk.CTkLabel(self,
                                    text="Email:",
                                    width=134,
                                    height=58,
                                    **Styles.label_styles["title2"])
        Email_Label.place(x=11, y=72)
        self.email = ctk.CTkEntry(self,
                                width=346,
                                height=50,
                                **Styles.entry_styles["default"])
        self.email.place(x=11, y=135)
        
        self.email_warning = ctk.CTkLabel(self, text="", width=140, height=24, **Styles.label_styles["error_title"])
        self.email_warning.place(x=20, y=198)
#----------------------------------------------------------------------------------------------------------
        password_Label = ctk.CTkLabel(self,
                                    text="Password:",
                                    width=235,
                                    height=58,
                                    **Styles.label_styles["title2"])
        password_Label.place(x=11, y=217)
        password_Entry = ctk.CTkEntry(self,
                                    textvariable=self.password,
                                    show="*",
                                    width=334,
                                    height=41,
                                    **Styles.entry_styles["default"])
        password_Entry.place(x=11, y=275)
        self.password_warning = ctk.CTkLabel(self, text="", width=140, height=24, **Styles.label_styles["error_title"])
        self.password_warning.place(relx=182, rely=24)
        
#------------------------------------------------------------------------------------------------------
        Body_Weight_Increase = ctk.CTkButton(self,
                                            text="+",
                                            width=48,
                                            height=50,
                                            **Styles.button_styles["Medium"],
                                            command=lambda: self.body_Weight.set(self.body_Weight.get() + 1))
        Body_Weight_Increase.place(x=202, y=404)
        
        Body_Weight_Label = ctk.CTkLabel(self,
                                    text="Body Weight: ",
                                    width=171,
                                    height=58,
                                    **Styles.label_styles["subtitle2"])
        Body_Weight_Label.place(x=68, y=346)
        body_Weight = ctk.CTkEntry(self,
                                    textvariable=self.body_Weight,
                                    width=98,
                                    height=50,
                                    **Styles.entry_styles["default"])
        body_Weight.place(x=92, y=404)
        self.weight_warning = ctk.CTkLabel(self, text="",width=156, height=24, **Styles.label_styles["error_title"])
        self.weight_warning.place(x=52, y=465)
        
        Body_Weight_Decrease = ctk.CTkButton(self,
                                            text="-",
                                            width=48,
                                            height=50,
                                            **Styles.button_styles["Medium"],
                                            command=lambda: self.body_Weight.set(self.body_Weight.get() - 1))
        Body_Weight_Decrease.place(x=30, y=404)
        #--------------------------------------------------------------------------
        Body_Height_Increase = ctk.CTkButton(self,
                                            text="+",
                                            width=48,
                                            height=50,
                                            **Styles.button_styles["Medium"],
                                            command=lambda: self.body_Height.set(self.body_Height.get() + 1))
        Body_Height_Increase.place(x=444, y=404)
        
        Body_Height_Label = ctk.CTkLabel(self,
                                    text="Body Height: ",
                                    width=164,
                                    height=58,
                                    **Styles.label_styles["subtitle2"])
        Body_Height_Label.place(x=310, y=346)
        
        body_Height = ctk.CTkEntry(self,
                                    textvariable=self.body_Height,
                                    width=98,
                                    height=50,
                                    **Styles.entry_styles["default"])
        body_Height.place(x=334, y=404)
        
        self.height_warning = ctk.CTkLabel(self, text="", width=153, height=24, **Styles.label_styles["error_title"])
        self.height_warning.place(x=305, y=465)
        
        Body_Height_Decrease = ctk.CTkButton(self,
                                            text="-",
                                            width=48,
                                            height=50,
                                            **Styles.button_styles["Medium"],
                                            command=lambda: self.body_Height.set(self.body_Height.get() - 1))
        Body_Height_Decrease.place(x=272, y=404)
        #------------------------------------------------------------------------------------------
        Age_Increase = ctk.CTkButton(self,
                                            text="+",
                                            width=48,
                                            height=50,
                                            **Styles.button_styles["Medium"],
                                            command=lambda: self.age.set(self.age.get() + 1))
        Age_Increase.place(x=691, y=404)

        Age_Label = ctk.CTkLabel(self,
                                    text="Body Height: ",
                                    width=130,
                                    height=58,
                                    **Styles.label_styles["subtitle2"])
        Age_Label.place(x=556, y=343)
        
        Age_Entry = ctk.CTkEntry(self,
                                    textvariable=self.age,
                                    width=98,
                                    height=50,
                                    **Styles.entry_styles["default"])
        Age_Entry.place(x=581, y=404)
        self.age_warning = ctk.CTkLabel(self, text="", width=128, height=24, **Styles.label_styles["error_title"])
        self.age_warning.place(x=556, y=465)
        
        
        Age_Decrease = ctk.CTkButton(self,
                                            text="-",
                                            width=48,
                                            height=50,
                                            **Styles.button_styles["Medium"],
                                            command=lambda: self.age.set(self.age.get() - 1))
        Age_Decrease.place(x=519, y=404)
        #---------------------------------------------------------------------------------------
        Activity_Label = ctk.CTkLabel(self,
                                    text="Activity:",
                                    width=184,
                                    height=58,
                                    **Styles.label_styles["title2"])
        Activity_Label.place(x=400, y=217)
        
        self.Activity = ctk.CTkComboBox(self,
                                            values= ["Basal Metabolic Rate (BMR)", 
                                                    "Sedentary: little or no exercise",
                                                    "Light: exercise 1-3 times/week",
                                                    "Moderate: exercise 4-5 times/week",
                                                    "Active: daily exercise or intense exercise 3-4 times/week",
                                                    "Very Active: intense exercise 6-7 times/week",
                                                    "Extra Active: very intense exercise daily, or physical job"],
                                            width=334,
                                            height=41,
                                            border_color="#4A90E2",
                                            bg_color="#2B2B2B",
                                            dropdown_fg_color="#2B2B2B",
                                            dropdown_text_color="white",
                                            text_color="white",
                                            button_color="grey",
                                            font=("Lato", 20, "bold"),
                                            dropdown_font=("Lato", 20, "bold"))
        self.Activity.place(x=411, y=275)
        
        Submit_Btn = ctk.CTkButton(self,
                                    text="Sign Up",
                                    width=270,
                                    height=60,
                                    **Styles.button_styles["Big"],
                                    command=self.Submit)
        Submit_Btn.place(relx=0.5, rely=0.9, anchor="center")