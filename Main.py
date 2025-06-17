# Importing the modules needed!
import os
import sys
from path_setup import add_frames_path, get_data_path
add_frames_path()
add_frames_path("Data_Side")

import customtkinter as ctk
import Styles  # type: ignore
import sqlite3
import Side_Functions  # type: ignore
from First_Interface import Sign_Up, Login, Report_Section  # type: ignore
from Calorie_Fitness import Program_setUp  # type: ignore
from Menu import mainMenu  # type: ignore
from PIL import Image

# Open database connections
Con, Cur = Side_Functions.openData(get_data_path("Users_Data.db"), "Data_Side/GYM&User_DATA.sql")
Con_Feed_Repo, Cur_Feed_Repo = Side_Functions.openData(get_data_path("Reports&Feedbacks.db"), "Data_Side/Reports&Feedbacks.sql")

# Set global appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Main_Window(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("BLACK GYM!!")
        self.configure(fg_color="#2B2B2B")
        
        self.First_Interface_Frame = ctk.CTkFrame(self, width=800, height=600)
        self.Create_First_InterFace()

        # Start with main menu
        self.Show_Main()
        self.protocol("WM_DELETE_WINDOW", self.cleanup_exit)

    def Create_First_InterFace(self):
        # Background image
        bkg_Image = ctk.CTkImage(dark_image=Image.open("Window_Images/First_BG.jpeg"), size=(800, 600))
        bg_label = ctk.CTkLabel(self.First_Interface_Frame, image=bkg_Image, text="", fg_color="transparent")
        bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Title
        Title_Label = ctk.CTkLabel(self.First_Interface_Frame, 
                                text="Welcome to THE BLACK GYM!!", 
                                   **Styles.label_styles["title1"])
        Title_Label.place(relx=0.50, rely=0.12, anchor="center")

        # Buttons
        Sign_up_Btn = ctk.CTkButton(self.First_Interface_Frame, text="Sign Up", 
                                    **Styles.button_styles["Big"], command=self.Show_Sign)
        Sign_up_Btn.place(relx=0.5, rely=0.34, relwidth=0.75, relheight=0.12, anchor="center")
        Sign_up_Btn.bind("<Enter>", lambda e: Sign_up_Btn.configure(cursor="hand2"))

        Login_Btn = ctk.CTkButton(self.First_Interface_Frame, text="Login", 
                                    **Styles.button_styles["Big"], command=self.Show_Login)
        Login_Btn.place(relx=0.5, rely=0.54, relwidth=0.75, relheight=0.12, anchor="center")
        Login_Btn.bind("<Enter>", lambda e: Login_Btn.configure(cursor="hand2"))

        Exit_Btn = ctk.CTkButton(self.First_Interface_Frame, text="Exit", 
                                 **Styles.button_styles["Danger!"], command=self.Check_if_sure)
        Exit_Btn.place(relx=0.5, rely=0.74, relwidth=0.75, relheight=0.12, anchor="center")
        Exit_Btn.bind("<Enter>", lambda e: Exit_Btn.configure(cursor="hand2"))

        Feedback_Btn = ctk.CTkButton(self.First_Interface_Frame, text="Report Problem", 
                                     **Styles.button_styles["Small"], command=self.Show_Report)
        Feedback_Btn.place(relx=0.5, rely=0.9, relwidth=0.3, relheight=0.12, anchor="center")
        Feedback_Btn.bind("<Enter>", lambda e: Feedback_Btn.configure(cursor="hand2"))

        # Back button for returning from Sign/Login/Report to main interface
        self.Create_back_btn(self.Show_Report, self.First_Interface_Frame, 20, 511)
        self.Create_back_btn(self.Show_Login, self.First_Interface_Frame, 20, 511)
        self.Create_back_btn(self.Show_Sign, self.First_Interface_Frame, 20, 511)

    def Create_back_btn(self, go_back_func, frame, x, y):
        back_btn = ctk.CTkButton(frame, width=127, height=37, text="Back ⬅",
                                 **Styles.button_styles["Small"], command=go_back_func)
        back_btn.place(x=x, y=y)

    def Show_Page(self, Page):
        for widget in self.winfo_children():
            if isinstance(widget, ctk.CTkFrame):
                widget.place_forget()
        Page.place(relx=0, rely=0, relwidth=1, relheight=1)

    def Show_Program(self):
        if not hasattr(self, "Showing_Program"):
            self.Showing_Program = Program_setUp(self, self.Show_Main)
        self.geometry("1000x600")
        self.Show_Page(self.Showing_Program)

    def Show_Main(self):
        if not hasattr(self, "Showing_Main"):
            self.Showing_Main = mainMenu(self)
        self.geometry("1000x600")
        self.Show_Page(self.Showing_Main)

    def Show_Sign(self):
        if not hasattr(self, "Showing_Sign"):
            self.Showing_Sign = Sign_Up(self, self.Show_Login)
        self.Show_Page(self.Showing_Sign)

    def Show_Report(self):
        if not hasattr(self, "Showing_Report"):
            self.Showing_Report = Report_Section(self)
        self.Show_Page(self.Showing_Report)

    def Show_Login(self):
        if not hasattr(self, "Showing_Login"):
            self.Showing_Login = Login(self, self.Show_Program, self.Show_Main)
        self.Show_Page(self.Showing_Login)

    def cleanup_exit(self):
        Con.close()
        Con_Feed_Repo.close()
        self.destroy()

    def Check_if_sure(self):
        self.Sure_Windows = ctk.CTkToplevel()
        self.Sure_Windows.geometry("400x250")
        self.Sure_Windows.title("Are you sure?")
        ctk.CTkLabel(self.Sure_Windows, text="Are you sure \nyou want to proceed?", 
                     **Styles.label_styles["subtitle2"]).pack(pady=10)
        ctk.CTkButton(self.Sure_Windows, text="Yes", **Styles.button_styles["Small"], 
                    command=lambda: self.cleanup_exit()).pack(padx=10, pady=10)
        ctk.CTkButton(self.Sure_Windows, text="No", **Styles.button_styles["Small"], 
                    command=self.Sure_Windows.destroy).pack(padx=5, pady=5)
        self.Sure_Windows.attributes("-topmost", True)

# Run the app
Main = Main_Window()
Main.mainloop()
