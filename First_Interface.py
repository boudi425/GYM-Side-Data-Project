import customtkinter as ctk
import Styles
import datetime
import sqlite3
import Side_Functions
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
Names = [name[0] for name in Cur.execute("SELECT Name FROM Users").fetchall()]
Emails = [email[0] for email in Cur.execute("SELECT Email FROM Users").fetchall()]

class Sign_Up(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.username = ctk.StringVar()
        self.password = ctk.StringVar()
        self.email = ctk.StringVar()
        self.body_Weight = ctk.StringVar(value=0)
        self.body_Height = ctk.StringVar(value=0)
        self.age = ctk.StringVar(value=0)
        self.Activity = ctk.StringVar(value="Moderate: exercise 4-5 times/week")
        self.Status = False
        self.Create_Sign_Up_Frame()
        
    def Error_Popup_Window(self, Label_Text, Button_Text):
        root = ctk.CTkToplevel()
        root.geometry("250x150")
        root.title("Error")
        ctk.CTkLabel(root, text=Label_Text, **Styles.label_styles["subtitle2"])
        ctk.CTkButton(root, text=Button_Text, **Styles.button_styles["Small"], command=root.destroy)

    def Submit(self):
        valid = True
        
        if not Side_Functions.check_empty(self.username, self.username_warning, "⚠ Username required"):
            valid = False
        elif self.username.get().capitalize() in Names:
            self.username_warning.configure(text="⚠ Username is already Taken")
            self.username_warning.update()
            valid = False
        #---------------------------------------------------------------------------------------------------
        if not Side_Functions.check_empty(self.password, self.password_warning, "⚠ Password required"):
            valid = False
        if not Side_Functions.check_empty(self.body_Weight, self.weight_warning, "⚠ Weight required"):
            valid = False
        elif self.body_Weight.get().isalpha():
            self.weight_warning.configure(text="⚠ Enter Numbers Only")
            valid = False
        elif int(self.body_Weight.get()) < 0:
            self.weight_warning.configure(text="⚠ Negative Numbers \naren't allowed")
            valid = False
            
        if not Side_Functions.check_empty(self.body_Height, self.height_warning, "⚠ Height required"):
            valid = False
        elif self.body_Height.get().isalpha():
            self.height_warning.configure(text="⚠ Enter Numbers Only")
            valid = False
        elif int(self.body_Height.get()) < 0:
            self.height_warning.configure(text="⚠ Negative Numbers \naren't allowed")
            valid = False
            
        if not Side_Functions.check_empty(self.email, self.email_warning, "⚠ Email required"):
            valid = False
        elif Side_Functions.suggest_email_domain(self.email.get()) != None:
            Domain = Side_Functions.suggest_email_domain(self.email.get())
            self.email_warning.configure(text=Domain)
        elif self.email.get() in Emails:
            self.email_warning.configure(text="⚠ Email is already Taken")
            valid = False
            
        if not Side_Functions.check_empty(self.age, self.age_warning, "⚠ Age required"):
            valid = False
        elif self.age.get().isalpha():
            self.age_warning.configure(text="⚠ Enter Numbers Only")
            valid = False
        elif int(self.age.get()) < 0:
            self.age_warning.configure(text="⚠ Negative Numbers \naren't allowed")
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
        userName = ctk.CTkEntry(self,
                                    textvariable=self.username,
                                    width=346,
                                    height=50,
                                    **Styles.entry_styles["default"])
        userName.place(x=405, y=134)
        
        self.username_warning = ctk.CTkLabel(self, text="", width=140, height=24, **Styles.label_styles["error_title"])
        self.username_warning.place(x=405, y=198)
#-------------------------------------------------------------------------------------------------------
        Email_Label = ctk.CTkLabel(self,
                                    text="Email:",
                                    width=134,
                                    height=58,
                                    **Styles.label_styles["title2"])
        Email_Label.place(x=11, y=72)
        email = ctk.CTkEntry(self,
                                textvariable= self.email,
                                width=346,
                                height=50,
                                **Styles.entry_styles["default"])
        email.place(x=11, y=135)
        
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
        """"fg_color": "#F5F5F5",
        "border_color": "#CCCCCC",
        "corner_radius": 8,
        "text_color": "#333333",
        "font": ("Lato", 28, "bold")
        """
        password_show_btn = ctk.CTkButton(self,
                                        text="👁",
                                        font=("Lato", 30, "bold"),
                                        width=48,
                                        height=50,
                                        fg_color="#000000",
                                        bg_color="#2B2B2B",
                                        border_color="#CCCCCC",
                                        corner_radius=5,
                                        hover_color= "#FFE23D",
                                        command=lambda: password_Entry.configure(show="")
                                        )
        password_show_btn.place(x=345, y=271)
        self.password_warning = ctk.CTkLabel(self, text="", width=140, height=24, **Styles.label_styles["error_title"])
        self.password_warning.place(x=20, y=321)
        
#------------------------------------------------------------------------------------------------------
        Body_Weight_Increase = ctk.CTkButton(self,
                                            text="+",
                                            width=48,
                                            height=50,
                                            **Styles.button_styles["Medium"],
                                            command=lambda: self.body_Weight.set(int(self.body_Weight.get()) + 1))
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
                                            command=lambda: self.body_Weight.set(int(self.body_Weight.get()) - 1))
        Body_Weight_Decrease.place(x=30, y=404)
        #--------------------------------------------------------------------------
        Body_Height_Increase = ctk.CTkButton(self,
                                            text="+",
                                            width=48,
                                            height=50,
                                            **Styles.button_styles["Medium"],
                                            command=lambda: self.body_Height.set(int(self.body_Height.get()) + 1))
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
                                            command=lambda: self.body_Height.set(int(self.body_Height.get()) - 1))
        Body_Height_Decrease.place(x=272, y=404)
        #------------------------------------------------------------------------------------------
        Age_Increase = ctk.CTkButton(self,
                                            text="+",
                                            width=48,
                                            height=50,
                                            **Styles.button_styles["Medium"],
                                            command=lambda: self.age.set(int(self.age.get()) + 1))
        Age_Increase.place(x=691, y=404)

        Age_Label = ctk.CTkLabel(self,
                                    text="Age: ",
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
                                            command=lambda: self.age.set(int(self.age.get()) - 1))
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
                                            state="readonly",
                                            border_color="#4A90E2",
                                            bg_color="#2B2B2B",
                                            dropdown_fg_color="#2B2B2B",
                                            dropdown_text_color="white",
                                            text_color="white",
                                            button_color="grey",
                                            font=("Lato", 20, "bold"),
                                            dropdown_font=("Lato", 20, "bold"))
        self.Activity.place(x=411, y=275)
        self.Activity.set("Moderate: exercise 4-5 times/week")
        Submit_Btn = ctk.CTkButton(self,
                                    text="Sign Up",
                                    width=270,
                                    height=60,
                                    **Styles.button_styles["Big"],
                                    command=self.Submit)
        Submit_Btn.place(relx=0.5, rely=0.9, anchor="center")
class Login(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.Email = ctk.StringVar()
        self.Password = ctk.StringVar()
        self.Stay_logged = False
        self.Accept_Terms = False
        self.Token = ""
        self.Create_Login_Frame()
        
    def Submit(self):
        valid = True 
        if not Side_Functions.check_empty(self.Email.get(), self.Email_warning, "⚠ Email required"):
            valid = False
        elif self.Email.get() in Emails:
            password = Cur.execute("SELECT Password FROM Users WHERE Email = ?", (self.Email.get())).fetchone()
            if not Side_Functions.verify_password(self.Password.get(), password[0]):
                self.Password_waring.configure(text="⚠ Incorrect Password")
                valid = False
        if not self.Terms_and_Privacy_Cb:
            self.Submit_Btn_warning.configure(text="⚠ Must Accept our Terms.")
            valid = False
        if self.Stay_Logged_Cb:
            Token = Side_Functions.generate_token()
            with open("auth_token.text", "w") as f:
                f.write(Token)
                Cur.execute("UPDATE Users SET token = ? WHERE Email = ?", (Token, self.Email.get()))
                Con.commit()
        if valid:
            self.destroy()
            self.Access()
    def Access(self):
        self.Access_Gained = ctk.CTkToplevel()
        self.Access_Gained.geometry("400x200")
        self.Access_Gained.title("Processing...")
        self.Bar = ctk.CTkProgressBar(self.Access_Gained, width=300, progress_color="green",
                        corner_radius=6)
        self.Bar.pack(pady=50)
        self.Bar.set(0)
        
    def Loading_Simulation(self, value=0):
        if value <= 1:
            self.Bar.set(value)
            self.Access_Gained.after(100, lambda: self.Loading_Simulation(value + 0.02))
        else:
            Loading_Text = ctk.CTkLabel(self.Access_Gained, text="Entering Main Menu...", **Styles.label_styles["subtitle2"])
            Loading_Text.place(pady=10)
            self.Access_Gained.after(2000, self.Access_Gained.destroy())
            
    def Create_Login_Frame(self):
        Login_Label = ctk.CTkLabel(self, 
                                text="Login",
                                width=147,
                                height=58,
                                **Styles.label_styles["title2"])
        Login_Label.place(x=293, y=20, anchor="center")
        
        Email_Label = ctk.CTkLabel(self, text="Email",
                                width=134,
                                height=58,
                                **Styles.label_styles["subtitle2"])
        Email_Label.place(x=209, y=66)
        
        Email_entry = ctk.CTkEntry(self, textvariable=self.Email,
                                width=346, height=50,
                                **Styles.entry_styles["default"])
        Email_entry.place(x=209, y=129, anchor="center")
        
        self.Email_warning = ctk.CTkLabel(self, width=140, height=24, text="",
                                        **Styles.label_styles["error_title"])
        self.Email_warning.place(x=218, y=192)
        
        Password_Label = ctk.CTkLabel(self, width=235, height=58, text="Password",
                                    **Styles.label_styles["subtitle2"])
        Password_Label.place(x=209, y=221)
        
        Password_entry = ctk.CTkEntry(self, textvariable=self.Password, show="*",
                                    width=334, height=41,
                                    **Styles.entry_styles["default"])
        Password_entry.place(x=209, y=279, anchor="center")
        password_show_btn = ctk.CTkButton(self,
                                        text="👁",
                                        font=("Lato", 30, "bold"),
                                        width=48,
                                        height=50,
                                        fg_color="#000000",
                                        bg_color="#2B2B2B",
                                        border_color="#CCCCCC",
                                        corner_radius=5,
                                        hover_color= "#FFE23D",
                                        command=lambda: Password_entry.configure(show="")
                                        )
        password_show_btn.place(x=543, y=275)
        
        self.Password_waring = ctk.CTkLabel(self, text="", width=182, height=24,
                                            **Styles.label_styles["error_title"])
        self.Password_waring.place(x=218, y=325, anchor="center")
        
        self.Terms_and_Privacy_Cb = ctk.CTkCheckBox(self, width=40, height=40, **Styles.checkBox["Box1"])
        self.Terms_and_Privacy_Cb.place(x=220, y=360)
        
        Terms_and_Privacy_text = ctk.CTkLabel(self, width=355, height=48,
                                            text="Accept our terms and conditions and \n privacy statement",
                                            **Styles.label_styles["subtitle"])
        Terms_and_Privacy_text.place(x=274, y=357)
        
        self.Stay_Logged_Cb = ctk.CTkCheckBox(self, width=40, height=40, **Styles.checkBox["Box1"])
        self.Stay_Logged_Cb.place(x=220, y=420)
        
        Stay_Logged_Text = ctk.CTkLabel(self, width=142, height=24,
                                            text="Stay Logged in",
                                            **Styles.label_styles["subtitle"])
        Stay_Logged_Text.place(x=274, y=428)
        
        Submit_Btn = ctk.CTkButton(self, width=250, height=60,
                                text="LOGIN", **Styles.button_styles["Big"],
                                command=lambda: self.Submit())
        Submit_Btn.place(x=233, y=480)
        
        self.Submit_Btn_warning = ctk.CTkLabel(self, text="", 
                                            width=232, height=24,
                                            **Styles.label_styles["error_title"])
        self.Submit_Btn_warning.place(x=242, y=548)
        