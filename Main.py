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
class Sign_Up(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.Sign_Up_Frame = ctk.CTkFrame(self, width=800, height=600)
        self.Create_Sign_Up_Frame()
        self.username = ""
        self.password = ""
        self.email = ""
        self.body_Weight = ctk.IntVar(value=0)
        self.body_Height = ctk.IntVar(value=0)
        self.age = ctk.IntVar(value=0)
        self.Activity = ""
        self.Status = False
    def Error_Popup_Window(self, Label_Text, Button_Text):
        root = ctk.CTkToplevel()
        root.geometry("250x150")
        root.title("Error")
        ctk.CTkLabel(root, text=Label_Text, **Styles.label_styles["subtitle2"]).pack(pady=10)
        ctk.CTkButton(root, text=Button_Text, **Styles.button_styles["Small"], command=root.destroy).pack(pady=10)
    def Insert_Data(self, Name, Password, Email, Body_weight, Body_Height, Age, Activity, Status=False):
        name = self.username.get() if self.username.get() != "" else self.Error_Popup_Window("Please Enter your Username.", "Close")
        password = self.password.get() if self.password.get() != "" else self.Error_Popup_Window("Please Enter your Password.", "Close")
        email = self.email.get() if self.email.get() != "" else self.Error_Popup_Window("Please Enter your Email.", "Close")
        Body_weight = self.body_Weight.get() if self.body_Weight.get() != 0 else self.Error_Popup_Window("Please Enter your Weight.", "Close")
        Body_height = self.body_Height.get() if self.body_Height.get() != 0 else self.Error_Popup_Window("Please Enter your Height.", "Close")
        age = self.age.get() if self.age.get() != 0 else self.Error_Popup_Window("Please Enter your Age.", "Close") 
        Activity = self.Activity.get()
        status = self.Status
        
    def Increase(self, Num):
        current = Num.get()
        Num.set(current + 1)
    def Decrease(self, Num):
        current = Num.get()
        Num.set(current - 1)
    
    def Create_Sign_Up_Frame(self):
        Title_Label = ctk.CTkLabel(self.Sign_Up_Frame, 
                                text="Sign Up To Experience All Our WORK!"
                                **Styles.label_styles["title2"])
        Title_Label.place(relx=0.50, rely=0.12, anchor="center")
        
        User_Name_Label = ctk.CTkLabel(self.Sign_Up_Frame,
                                    text="Username:"
                                    **Styles.label_styles["subtitle2"])
        User_Name_Label.grid(row=2, column=1, padx=10, pady=10)
        self.username = ctk.CTkEntry(self.Sign_Up_Frame
                                    **Styles.entry_styles["default"])
        self.username.grid(row=3, column=1, padx=10, pady=10)
        
        password_Label = ctk.CTkLabel(self.Sign_Up_Frame,
                                    text="Password:"
                                    **Styles.label_styles["subtitle2"])
        password_Label.grid(row=2, column=3, padx=10, pady=10)
        self.password = ctk.CTkEntry(self.Sign_Up_Frame,
                                    show="*",
                                    **Styles.entry_styles["default"])
        self.password.grid(row=3, column=3, padx=10, pady=10)
        
        Body_Weight_Increase = ctk.CTkButton(self.Sign_Up_Frame,
                                            text="+"
                                            **Styles.button_styles["Medium"],
                                            command=self.Increase(self.body_Weight))
        Body_Weight_Increase.grid(row=5, column=1, padx=5, pady=5)
        
        Body_Weight_Label = ctk.CTkLabel(self.Sign_Up_Frame,
                                    text="Body Weight: "
                                    **Styles.label_styles["subtitle2"])
        Body_Weight_Label.grid(row=4, column=3, padx=10, pady=5)
        self.body_Weight = ctk.CTkEntry(self.Sign_Up_Frame,
                                    textvariable=self.body_Weight
                                    **Styles.entry_styles["default"])
        self.body_Weight.grid(row=4, column=3, padx=5, pady=5)
        
        Body_Weight_Decrease = ctk.CTkButton(self.Sign_Up_Frame,
                                            text="-"
                                            **Styles.button_styles["Medium"],
                                            command=self.Decrease(self.body_Weight))
        Body_Weight_Decrease.grid(row=5, column=5, padx=5, pady=5)
        #--------------------------------------------------------------------------
        Body_Height_Increase = ctk.CTkButton(self.Sign_Up_Frame,
                                            text="+"
                                            **Styles.button_styles["Medium"],
                                            command=self.Increase(self.body_Height))
        Body_Height_Increase.grid(row=5, column=7, padx=5, pady=5)
        
        Body_Height_Label = ctk.CTkLabel(self.Sign_Up_Frame,
                                    text="Body Height: "
                                    **Styles.label_styles["subtitle2"])
        Body_Height_Label.grid(row=4, column=9, padx=10, pady=5)
        self.body_Height = ctk.CTkEntry(self.Sign_Up_Frame,
                                    textvariable=self.body_Height
                                    **Styles.entry_styles["default"])
        self.body_Height.grid(row=5, column=9, padx=5, pady=5)

        Body_Height_Decrease = ctk.CTkButton(self.Sign_Up_Frame,
                                            text="-"
                                            **Styles.button_styles["Medium"],
                                            command=self.Decrease(self.body_Height))
        Body_Height_Decrease.grid(row=5, column=11, padx=5, pady=5)
        #------------------------------------------------------------------------------------------
        Age_Increase = ctk.CTkButton(self.Sign_Up_Frame,
                                            text="+"
                                            **Styles.button_styles["Medium"],
                                            command=self.Increase(self.age))
        Age_Increase.grid(row=5, column=13, padx=5, pady=5)

        Age_Label = ctk.CTkLabel(self.Sign_Up_Frame,
                                    text="Body Height: "
                                    **Styles.label_styles["subtitle2"])
        Age_Label.grid(row=4, column=15, padx=10, pady=5)
        self.age = ctk.CTkEntry(self.Sign_Up_Frame,
                                    textvariable=self.age
                                    **Styles.entry_styles["default"])
        self.age.grid(row=5, column=15, padx=5, pady=5)

        Age_Decrease = ctk.CTkButton(self.Sign_Up_Frame,
                                            text="-"
                                            **Styles.button_styles["Medium"],
                                            command=self.Decrease(self.age))
        Age_Decrease.grid(row=5, column=17, padx=5, pady=5)
        #---------------------------------------------------------------------------------------
        Activity_Label = ctk.CTkLabel(self.Sign_Up_Frame,
                                    text="Activity:",
                                    **Styles.label_styles["subtitle2"])
        Activity_Label.grid(row=7, column=15, padx=10, pady=5)
        
        self.Activity = ctk.CTkComboBox(self.Sign_Up_Frame,
                                            values= ["Basal Metabolic Rate (BMR)", 
                                                    "Sedentary: little or no exercise",
                                                    "Light: exercise 1-3 times/week",
                                                    "Moderate: exercise 4-5 times/week",
                                                    "Active: daily exercise or intense exercise 3-4 times/week",
                                                    "Very Active: intense exercise 6-7 times/week",
                                                    "Extra Active: very intense exercise daily, or physical job"],
                                            border_color="#4A90E2",
                                            bg_color="#2B2B2B",
                                            dropdown_fg_color="#2B2B2B",
                                            dropdown_text_color="white",
                                            text_color="white",
                                            button_color="grey",
                                            font=("Lato", 20, "bold"),
                                            dropdown_font=("Lato", 20, "bold"))
        self.Activity.grid(row=8, column=15, padx=10, pady=10)
        self.Activity.set("Moderate: exercise 4-5 times/week")
        
        Submit_Btn = ctk.CTkComboBox(self.Sign_Up_Frame,
                                    text="Sign Up",
                                    **Styles.button_styles["Big"],
                                    command=self.Insert_Data())
        Submit_Btn.grid(row=10, column=15, padx=10, pady=10)
class Main_Window(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("BLACK GYM!!")
        self.configure(fg_color="#2B2B2B")
        self.First_Interface_Frame = ctk.CTkFrame(self, width=800, height=600)
        
        self.Create_First_InterFace()
        
        self.Show_Page(self.First_Interface_Frame)
    def Create_First_InterFace(self):
        Title_Label = ctk.CTkLabel(self.First_Interface_Frame, 
                                text="Welcome to THE BLACK GYM!!", 
                                **Styles.label_styles["title"]
        )

        Title_Label.place(relx=0.50, rely=0.12, anchor="center")

        Sign_up_Btn = ctk.CTkButton(self.First_Interface_Frame, 
                                text="Sign Up", 
                                **Styles.button_styles["Big"],
        )
        Sign_up_Btn.place(relx=0.5, rely=0.34, relwidth=0.75 ,relheight=0.12,anchor="center")
        Sign_up_Btn.bind("<Enter>", lambda e: Sign_up_Btn.configure(cursor="hand2"))

        Sign_in_Btn = ctk.CTkButton(self.First_Interface_Frame, 
                                text="Sign In", 
                                **Styles.button_styles["Big"],
        )
        Sign_in_Btn.place(relx=0.5, rely=0.54, relwidth=0.75 ,relheight=0.12 ,anchor="center")
        Sign_in_Btn.bind("<Enter>", lambda e: Sign_in_Btn.configure(cursor="hand2"))

        Exit_Btn = ctk.CTkButton(self.First_Interface_Frame, 
                                text="Exit", 
                                fg_color= "#4A90E2",
                                bg_color= "#2B2B2B",
                                hover_color= "#ff3f3f",
                                text_color= "white",
                                corner_radius= 14,
                                font= ("Lato", 40, "bold"),
                                border_width= 0,
                                command= lambda: self.Show_Page(self.Test_Frame)
        )
        Exit_Btn.place(relx=0.5, rely=0.74, relwidth=0.75 ,relheight=0.12 ,anchor="center")
        Exit_Btn.bind("<Enter>", lambda e: Exit_Btn.configure(cursor="hand2"))

        Feedback_Btn = ctk.CTkButton(self.First_Interface_Frame, 
                                text="Feedback", 
                                **Styles.button_styles["Small"]
        )
        Feedback_Btn.place(relx=0.5, rely=0.9, relwidth=0.3 ,relheight=0.12 ,anchor="center")
        Feedback_Btn.bind("<Enter>", lambda e: Feedback_Btn.configure(cursor="hand2"))
    def Show_Page(self, Page):
        for widget in self.winfo_children():
            if isinstance(widget, ctk.CTkFrame):
                widget.place_forget()
        Page.place(x=0, y=0)
Main = Main_Window()
#Main.mainloop()
Testing = Sign_Up()
Testing.mainloop()