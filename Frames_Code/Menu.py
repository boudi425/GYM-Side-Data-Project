import customtkinter as ctk
import Styles
from User_session import load_session, save_session, user_session
import Side_Functions
import os
import sys
import sqlite3
import webbrowser
from PIL import Image
class mainMenu(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.Create_mainMenu_Frame()
    def Create_mainMenu_Frame(self):
        Data_Load = load_session()
        ctk.CTkLabel(self, text="BLACK GYM Main Menu", **Styles.label_styles["Menu_title"]).place(x=24, y=11)
        #IMAGES!!!!
        Logout_Image = ctk.CTkImage(dark_image=Image.open("Window_Images/logout.png"), size=(24, 24))
        Profile_Image = ctk.CTkImage(dark_image=Image.open("Window_Images/Profile.png"), size=(24, 24))
        Settings_Image = ctk.CTkImage(dark_image=Image.open("Window_Images/Sett.png"), size=(24, 24))
        Calorie_Image = ctk.CTkImage(dark_image=Image.open("Window_Images/Cal.png"), size=(30, 30))
        Exercise_Image = ctk.CTkImage(dark_image=Image.open("Window_Images/Exe.png"), size=(30, 30))
        Goal_Image = ctk.CTkImage(dark_image=Image.open("Window_Images/Progress.png"), size=(30, 30))
        Plan_Image = ctk.CTkImage(dark_image=Image.open("Window_Images/Plan.png"), size=(30, 30))
        Feedback_Image = ctk.CTkImage(dark_image=Image.open("Window_Images/Feedback.png"), size=(30, 30))
        #---------------------------------------------------------------------------------------------------------
        
        self.In_frame = ctk.CTkFrame(self, width=768, height=520, fg_color="gray20", border_width=2, border_color="white")
        self.In_frame.place(x=220, y=70)
        
        Profile_Button = ctk.CTkButton(self, text="Profile", image=Profile_Image, **Styles.button_styles["First"], 
                    width=150,
                    height=50,
                    compound="left")
        Profile_Button.place(x=500, y=11)
        Profile_Button.bind("<Enter>", lambda e: Profile_Button.configure(cursor="hand2"))
        
        Settings_Btn = ctk.CTkButton(self, text=" Settings", image=Settings_Image, **Styles.button_styles["Second"],
                    width=150,
                    height=50,
                    compound="left")
        Settings_Btn.place(x=672, y=11)
        Settings_Btn.bind("<Enter>", lambda e: Settings_Btn.configure(cursor="hand2"))
        
        Logout_Btn = ctk.CTkButton(self, text=" Logout", image=Logout_Image, **Styles.button_styles["Third"],
                    width=150,
                    height=50,
                    compound="left")
        Logout_Btn.place(x=840, y=11)
        Logout_Btn.bind("<Enter>", lambda e: Logout_Btn.configure(cursor="hand2"))
        
        Plans_Btn = ctk.CTkButton(self, text="My Plan", **Styles.button_styles["Fourth"],
                                image=Plan_Image,
                                width=184,
                                height=50,
                                compound="left")
        Plans_Btn.place(x=24, y=110)
        Plans_Btn.bind("<Enter>", Plans_Btn.configure(cursor="hand2"))
        
        Calorie_Btn = ctk.CTkButton(self, text="Calories", **Styles.button_styles["First"],
                                image=Calorie_Image,
                                width=184,
                                height=50,
                                compound="left")
        Calorie_Btn.place(x=24, y=190)
        Calorie_Btn.bind("<Enter>", Calorie_Btn.configure(cursor="hand2"))
        
        Exercise_Btn = ctk.CTkButton(self, text="Exercises", **Styles.button_styles["Second"],
                                    image=Exercise_Image,
                                    width=184,
                                    height=50,
                                    compound="left")
        Exercise_Btn.place(x=24, y=270)
        Exercise_Btn.bind("<Enter>", Exercise_Btn.configure(cursor="hand2"))
        
        Goal_Btn = ctk.CTkButton(self, text="Journey", **Styles.button_styles["Small"],
                                    image=Goal_Image,
                                    width=184,
                                    height=50,
                                    compound="left")
        Goal_Btn.place(x=24, y=350)
        Goal_Btn.bind("<Enter>", Goal_Btn.configure(cursor="hand2"))
        
        
        Feedback_Btn = ctk.CTkButton(self, text="Rate us!", **Styles.button_styles["Fifth"],
                                    image=Feedback_Image,
                                    width=184,
                                    height=50,
                                    compound="left")
        Feedback_Btn.place(x=24, y=528)
        Feedback_Btn.bind("<Enter>", Feedback_Btn.configure(cursor="hand2"))
        