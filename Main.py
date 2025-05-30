import customtkinter as ctk
import Styles
import datetime
import sqlite3
import Side_Functions
from First_Interface import Sign_Up, Login, Feedback
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

class Main_Window_First_Interface(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("BLACK GYM!!")
        self.configure(fg_color="#2B2B2B")
        self.First_Interface_Frame = ctk.CTkFrame(self, width=800, height=600)
        self.Showing_Login = Login(self)
        self.Showing_Sign_Up = Sign_Up(self)
        self.Create_back_btn(self.Showing_Login, self.Showing_Sign_Up, 20, 511)
        self.Create_back_btn(self.Showing_Sign_Up, self.First_Interface_Frame, 20, 511)
        self.Create_First_InterFace()
        
        self.Show_Page(self.First_Interface_Frame)
    def Create_First_InterFace(self):
        Title_Label = ctk.CTkLabel(self.First_Interface_Frame, 
                                text="Welcome to THE BLACK GYM!!", 
                                **Styles.label_styles["title1"]
        )

        Title_Label.place(relx=0.50, rely=0.12, anchor="center")

        Sign_up_Btn = ctk.CTkButton(self.First_Interface_Frame, 
                                text="Sign Up", 
                                **Styles.button_styles["Big"],
                                command=lambda: self.Show_Page(self.Showing_Sign_Up)
        )
        Sign_up_Btn.place(relx=0.5, rely=0.34, relwidth=0.75 ,relheight=0.12,anchor="center")
        Sign_up_Btn.bind("<Enter>", lambda e: Sign_up_Btn.configure(cursor="hand2"))

        Sign_in_Btn = ctk.CTkButton(self.First_Interface_Frame, 
                                text="Login", 
                                **Styles.button_styles["Big"],
                                command=lambda: self.Show_Page(self.Showing_Login)
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
                                text="Report Problem", 
                                **Styles.button_styles["Small"]
        )
        Feedback_Btn.place(relx=0.5, rely=0.9, relwidth=0.3 ,relheight=0.12 ,anchor="center")
        Feedback_Btn.bind("<Enter>", lambda e: Feedback_Btn.configure(cursor="hand2"))
    def Show_Page(self, Page):
        for widget in self.winfo_children():
            if isinstance(widget, ctk.CTkFrame):
                widget.place_forget()
        Page.place(relx=0, rely=0, relwidth=1, relheight=1)
    def Create_back_btn(self, master, Frame, x, y):
        back_btn = ctk.CTkButton(master, width=127, height=37, text="Back <-", 
                                **Styles.button_styles["Small"],
                                command=lambda: self.Show_Page(Frame))
        back_btn.place(x=x, y=y)
        
class Dashboard(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x800")
        self.title("Dashboard")
        self.Create_Dashboard()
    def Create_Dashboard(self):
        Test = ctk.CTkLabel(self, text="Still under developing...", width=500, height=500)
        Test.place(x=500, y=500, anchor="center")
Main = Main_Window_First_Interface()
Main.mainloop()
