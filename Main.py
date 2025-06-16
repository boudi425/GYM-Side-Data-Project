#Importing The modules needed!
import os
import sys
from path_setup import add_frames_path, get_data_path
add_frames_path()
add_frames_path("Data_Side")
#Adding the file paths

import customtkinter as ctk
import Styles # type: ignore
import sqlite3
import Side_Functions # type: ignore
from First_Interface import Sign_Up, Login, Report_Section # type: ignore
from Calorie_Fitness import Program_setUp # type: ignore
from Menu import mainMenu # type: ignore
from PIL import Image

#This will be the Main Interface (start up interface you can say also)
#I will Start with the basics
#Zero basic Set up
Con = sqlite3.connect(get_data_path("Users_Data.db"))
Cur = Con.cursor()
with open("Data_Side/GYM&User_DATA.sql", "r") as Table_Query:
    Cur.executescript(Table_Query.read())
    
Con_Feed_Repo = sqlite3.connect(get_data_path("Reports&Feedbacks.db"))
Cur_Feed_Repo = Con_Feed_Repo.cursor()
with open("Data_Side/Reports&Feedbacks.sql", "r") as query:
    Cur_Feed_Repo.executescript(query.read())
#First: Sign up Interface/Class

#Main window set up!
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class Main_Window(ctk.CTk):
    def __init__(self):
        #Installing every possible Frame
        super().__init__()
        self.geometry("800x600")
        self.title("BLACK GYM!!")
        self.configure(fg_color="#2B2B2B")
        self.First_Interface_Frame = ctk.CTkFrame(self, width=800, height=600)
        self.Showing_Login = Login(self, self.Show_Program, self.Show_mainMenu)
        self.Showing_Sign_Up = Sign_Up(self, self.Show_Login)
        self.Showing_mainMenu = mainMenu(self)
        self.Showing_Report = Report_Section(self)
        self.Showing_Program = Program_setUp(self, self.Show_mainMenu)
        
        self.Create_back_btn(self.Showing_Report, self.First_Interface_Frame, 20, 511)
        self.Create_back_btn(self.Showing_Login, self.Showing_Sign_Up, 20, 511)
        self.Create_back_btn(self.Showing_Sign_Up, self.First_Interface_Frame, 20, 511)
        self.Create_First_InterFace()
        
        #self.Show_Page(self.Showing_mainMenu)
        self.Show_mainMenu()
        self.protocol("WM_DELETE_WINDOW", Side_Functions.cleanup_exit)
    def Create_First_InterFace(self):
        #Main Window Frame with Main four buttons
        bkg_Image = ctk.CTkImage(dark_image=Image.open("Window_Images/First_BG.jpeg"), size=(800, 600))
        
        bg_label = ctk.CTkLabel(self.First_Interface_Frame, image=bkg_Image, text="", fg_color="transparent")
        bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)
        #image_path = "Black Gym Icon.jpeg"
        #pil_image = Image.open(image_path)
        
        #ctk_image = ctk.CTkImage(dark_image=pil_image, size=(150, 120))
        #image_label = ctk.CTkLabel(self, image=ctk_image, text="")
        #image_label.place(x=650, y=480)
    
        Title_Label = ctk.CTkLabel(self.First_Interface_Frame, 
                                text="Welcome to THE BLACK GYM!!", 
                                **Styles.label_styles["title1"]
        )

        Title_Label.place(relx=0.50, rely=0.12, anchor="center")

        Sign_up_Btn = ctk.CTkButton(self.First_Interface_Frame, 
                                text="Sign Up", 
                                **Styles.button_styles["Big"],
                                command=lambda: self.Show_Page(self.Showing_Sign_Up) # => Show the Sign up frame when clicked!
        )
        Sign_up_Btn.place(relx=0.5, rely=0.34, relwidth=0.75 ,relheight=0.12,anchor="center")
        Sign_up_Btn.bind("<Enter>", lambda e: Sign_up_Btn.configure(cursor="hand2"))

        Sign_in_Btn = ctk.CTkButton(self.First_Interface_Frame, 
                                text="Login", 
                                **Styles.button_styles["Big"],
                                command=lambda: self.Show_Page(self.Showing_Login) # => Show the Log in Frame when clicked!
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
                                command= lambda: self.Check_if_sure() # Check first if sure then if sure destroy!
        )
        Exit_Btn.place(relx=0.5, rely=0.74, relwidth=0.75 ,relheight=0.12 ,anchor="center")
        Exit_Btn.bind("<Enter>", lambda e: Exit_Btn.configure(cursor="hand2"))

        Feedback_Btn = ctk.CTkButton(self.First_Interface_Frame, 
                                text="Report Problem", 
                                **Styles.button_styles["Small"],
                                command=lambda: self.Show_Page(self.Showing_Report) # Show the report Frame
        )
        Feedback_Btn.place(relx=0.5, rely=0.9, relwidth=0.3 ,relheight=0.12 ,anchor="center")
        Feedback_Btn.bind("<Enter>", lambda e: Feedback_Btn.configure(cursor="hand2"))
    def Show_Page(self, Page):
        #See every possible widget and then forget/destroy
        for widget in self.winfo_children():
            if isinstance(widget, ctk.CTkFrame):
                widget.place_forget()
        Page.place(relx=0, rely=0, relwidth=1, relheight=1) # Show the Selected Frame after!
    def Create_back_btn(self, master, Frame, x, y):
        #Create a back button that makes the user back to the last frame! 
        back_btn = ctk.CTkButton(master, width=127, height=37, text="Back ⬅", 
                                **Styles.button_styles["Small"],
                                command=lambda: self.Show_Page(Frame))
        back_btn.place(x=x, y=y)
        
    def Show_Login(self):
        #Making this because the self.switch() => See in the First_Interface!
        self.Show_Page(self.Showing_Login)
        
    def Show_Program(self):
        #This is similar but, I just wanted more space for making the design!
        self.geometry("1000x600")
        self.Show_Page(self.Showing_Program)
    
    def Show_mainMenu(self):
        self.geometry("1000x600")
        self.Show_Page(self.Showing_mainMenu)
        
    def Destroy_Everything(self, additional_Top):
        #This is here because when the user exits everything get destroyed!
        additional_Top.destroy()
        for Widget in self.winfo_children():
            Widget.place_forget()
        self.destroy()
        
    def Check_if_sure(self):
        #Creating if sure Window with simple code that if yes then destroy everything if not just destroy the top!
        self.Sure_Windows = ctk.CTkToplevel()
        self.Sure_Windows.geometry("400x250")
        self.Sure_Windows.title("Are you sure?")
        ctk.CTkLabel(self.Sure_Windows, text="Are you sure \nyou want to proceed?: ", **Styles.label_styles["subtitle2"]).pack(pady=10)
        ctk.CTkButton(self.Sure_Windows, text="Yes", **Styles.button_styles["Small"], command=lambda: self.Destroy_Everything(self.Sure_Windows)).pack(padx=10, pady=10)
        ctk.CTkButton(self.Sure_Windows, text="No", **Styles.button_styles["Small"], command= self.Sure_Windows.destroy).pack(padx=5, pady=5)
        self.Sure_Windows.attributes("-topmost", True) # => Make the top window shows at Top

#Running the script!
Main = Main_Window()
Main.mainloop()
