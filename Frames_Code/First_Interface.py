import os
import sys
from path_setup import get_data_path, add_frames_path
add_frames_path("Data_Side")
from db_connection import DBConnection # type: ignore
import customtkinter as ctk
import Styles
import sqlite3
import Side_Functions
from User_session import user_session, save_session, load_session
from PIL import Image
#Importing Main Modules needed!

#This will be the Main Interface (start up interface you can say also)
#I will Start with the basics
#Zero basic Set up
DB = DBConnection("Data_Side/Users_Data.db")
DB.execute("PRAGMA foreign_keys = ON;")
with open(get_data_path("GYM_Queries.sql"), "r") as file:
    sql_script = file.read()
    DB.executescript(sql_script)
Con_Feed_Repo, Cur_Feed_Repo = Side_Functions.openData(get_data_path("Reports&Feedbacks.db"), "Data_Side/Reports&Feedbacks.sql")
#First: Sign up Interface/Class

# // Main Window...
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
ctk.set_window_scaling(1)
ctk.set_widget_scaling(1)
class Sign_Up(ctk.CTkFrame):
    def __init__(self, master, switch_screen=None):
        super().__init__(master)
        self.switch_screen = switch_screen
        self.username = ctk.StringVar()
        self.password = ctk.StringVar()
        self.email = ctk.StringVar()
        self.body_Weight = ctk.StringVar(value="0")
        self.body_Height = ctk.StringVar(value="0")
        self.age = ctk.StringVar(value="0")
        self.Activity = ctk.StringVar(value="Moderate: exercise 4-5 times/week")
        self.Create_Sign_Up_Frame()

    def Error_Popup_Window(self, Label_Text, Button_Text):
        root = ctk.CTkToplevel()
        root.geometry("250x150")
        root.title("Error")
        ctk.CTkLabel(root, text=Label_Text, **Styles.label_styles["subtitle2"]).pack()
        ctk.CTkButton(root, text=Button_Text, **Styles.button_styles["Small"], command=root.destroy).pack()

    def Submit(self):
        Emails = [email[0] for email in DB.fetchall("SELECT Email FROM Users")]
        Names = [name[0] for name in DB.fetchall("SELECT Name FROM Users")]
        valid = True

        # Username
        if not Side_Functions.check_empty(self.userNameEntry, self.username_warning, "⚠ Username required"):
            valid = False
        elif self.userNameEntry.get().capitalize() in Names:
            self.username_warning.configure(text="⚠ Username is already Taken")
            valid = False
        elif len(self.userNameEntry.get()) > 32:
            self.username_warning.configure(text="⚠ Username is Too Long!")
            valid = False
        elif len(self.userNameEntry.get()) < 8:
            self.username_warning.configure(text="⚠ Username is Too Short!")
            valid = False

        # Password
        if not Side_Functions.check_empty(self.password_Entry, self.password_warning, "⚠ Password required"):
            valid = False
        elif len(self.password_Entry.get()) < 8:
            self.password_warning.configure(text="⚠ Password is Too Short!")
            valid = False
        # Weight
        if not Side_Functions.check_empty(self.body_WeightEntry, self.weight_warning, "⚠ Weight required"):
            valid = False
        else:
            try:
                if int(self.body_WeightEntry.get()) < 0:
                    self.weight_warning.configure(text="⚠ Negative Numbers \naren't allowed")
                    valid = False
            except ValueError:
                self.weight_warning.configure(text="⚠ Enter Numbers Only")
                valid = False

        # Height
        if not Side_Functions.check_empty(self.body_Height_Entry, self.height_warning, "⚠ Height required"):
            valid = False
        else:
            try:
                if int(self.body_Height.get()) < 0:
                    self.height_warning.configure(text="⚠ Negative Numbers \naren't allowed")
                    valid = False
            except ValueError:
                self.height_warning.configure(text="⚠ Enter Numbers Only")
                valid = False

        # Email
        if not Side_Functions.check_empty(self.emailEntry, self.email_warning, "⚠ Email required"):
            valid = False
        elif Side_Functions.suggest_email_domain(self.emailEntry.get()) is not None:
            self.email_warning.configure(text=Side_Functions.suggest_email_domain(self.emailEntry.get()))
            valid = False
        elif self.emailEntry.get() in Emails:
            self.email_warning.configure(text="⚠ Email is already Taken")
            valid = False

        # Age
        if not Side_Functions.check_empty(self.Age_Entry, self.age_warning, "⚠ Age required"):
            valid = False
        else:
            try:
                if int(self.Age_Entry.get()) < 0:
                    self.age_warning.configure(text="⚠ Negative Numbers \naren't allowed")
                    valid = False
            except ValueError:
                self.age_warning.configure(text="⚠ Enter Numbers Only")
                valid = False

        if valid:
            self.SignUp_Data_Management()

    def SignUp_Data_Management(self):
        try:
            DB.execute("""INSERT INTO Users(
                            Name, 
                            Password, 
                            Email, 
                            Body_Weight, 
                            Body_Height, 
                            Activity, 
                            Age) 
                        VALUES (?, ?, ?, ?, ?, ?, ?)""",
                        (
                            self.userNameEntry.get(),
                            self.password_Entry.get(),
                            self.emailEntry.get(),
                            int(self.body_WeightEntry.get()),
                            int(self.body_Height_Entry.get()),
                            self.Activity.get(),
                            int(self.Age_Entry.get())
                        ))
            if self.switch_screen:
                self.switch_screen()
        except Exception as e:
            self.Error_Popup_Window(f"Error: {e}", "Okay")
    def Create_Sign_Up_Frame(self):
        #Creating the frame Which contains every widgets needed (This is most one that takes code!)
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
        self.userNameEntry = ctk.CTkEntry(self,
                                    textvariable=self.username,
                                    width=346,
                                    height=50,
                                    **Styles.entry_styles["default"])
        self.userNameEntry.place(x=405, y=134)
        
        self.username_warning = ctk.CTkLabel(self, text="", width=140, height=24, **Styles.label_styles["error_title"])
        self.username_warning.place(x=405, y=198)
#-------------------------------------------------------------------------------------------------------
        Email_Label = ctk.CTkLabel(self,
                                    text="Email:",
                                    width=134,
                                    height=58,
                                    **Styles.label_styles["title2"])
        Email_Label.place(x=11, y=72)
        self.emailEntry = ctk.CTkEntry(self,
                                textvariable= self.email,
                                width=346,
                                height=50,
                                **Styles.entry_styles["default"])
        self.emailEntry.place(x=11, y=135)
        
        self.email_warning = ctk.CTkLabel(self, text="", width=140, height=24, **Styles.label_styles["error_title"])
        self.email_warning.place(x=20, y=198)
#----------------------------------------------------------------------------------------------------------
        password_Label = ctk.CTkLabel(self,
                                    text="Password:",
                                    width=235,
                                    height=58,
                                    **Styles.label_styles["title2"])
        password_Label.place(x=11, y=217)
        self.password_Entry = ctk.CTkEntry(self,
                                    textvariable=self.password,
                                    show="*",
                                    width=334,
                                    height=41,
                                    **Styles.entry_styles["default"])
        self.password_Entry.place(x=11, y=275)
        
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
                                        command=lambda: self.password_Entry.configure(show="")
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
        self.body_WeightEntry = ctk.CTkEntry(self,
                                    textvariable=self.body_Weight,
                                    width=98,
                                    height=50,
                                    **Styles.entry_styles["default"])
        self.body_WeightEntry.place(x=92, y=404)
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
        
        self.body_Height_Entry = ctk.CTkEntry(self,
                                    textvariable=self.body_Height,
                                    width=98,
                                    height=50,
                                    **Styles.entry_styles["default"])
        self.body_Height_Entry.place(x=334, y=404)
        
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
        
        self.Age_Entry = ctk.CTkEntry(self,
                                    textvariable=self.age,
                                    width=98,
                                    height=50,
                                    **Styles.entry_styles["default"])
        self.Age_Entry.place(x=581, y=404)
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
                                    command=self.Submit) # => Active the Submit button which handles the whole Frame logic!
        Submit_Btn.place(relx=0.5, rely=0.9, anchor="center")
class Login(ctk.CTkFrame):
    def __init__(self, master, switch_screen=None, Logged_switch_screen=None):
        # Setting up the vars needed!
        super().__init__(master)
        self.switch_screen = switch_screen
        self.Logged_switch_screen = Logged_switch_screen
        self.Email = ctk.StringVar()
        self.Password = ctk.StringVar()
        self.Stay_logged = ctk.BooleanVar()
        self.Accept_Terms = ctk.BooleanVar()
        self.Token = ""
        self.Create_Login_Frame()
    
    def Check_if_Logged(self):
        #This is here because if we actually have a token just as we are going to explain down, We can just login in immediately 
        try:
            with open("User_Out_Data/auth_token.txt", "r+") as f:
                #Trying to get the token and if there is an actual token we take it and show this top window asking if the user wants to proceed immediately 
                self.token = f.read().strip()
                if self.token:
                    self.Check_if_logged_window = ctk.CTkToplevel()
                    self.Check_if_logged_window.geometry("400x250")
                    self.Check_if_logged_window.title("Wish to proceed?")
                    ctk.CTkLabel(self.Check_if_logged_window, text="You already logged, Continue?", **Styles.label_styles["subtitle2"]).pack(pady=10)
                    ctk.CTkButton(self.Check_if_logged_window, text="Yes", **Styles.button_styles["Small"], command=lambda: self.Access()).pack(padx=10, pady=10)
                    ctk.CTkButton(self.Check_if_logged_window, text="No", **Styles.button_styles["Small"], command=lambda: self.Check_if_logged_window.destroy()).pack(padx=5, pady=5)
                    self.Check_if_logged_window.attributes("-topmost", True)
                else: 
                    self.Create_Login_Frame()
        except FileNotFoundError:
            return None
                
    def Submit(self):
        #Same as the sign up class
        Emails = [email[0] for email in DB.fetchall("SELECT Email FROM Users")]

        valid = True
        self.Email_warning.configure(text="")
        self.Password_warning.configure(text="")
        self.Submit_Btn_warning.configure(text="")

        # Email Validation
        if not Side_Functions.check_empty(self.Email_entry, self.Email_warning, "⚠ Email required"):
            valid = False
        elif self.Email_entry.get() not in Emails:
            self.Email_warning.configure(text="⚠ Email not found")
            valid = False
        else:
            # Password Validation
            password_data = DB.fetchone("SELECT Password FROM Users WHERE Email = ?", (self.Email_entry.get(),))
            if not Side_Functions.check_empty(self.Password_entry, self.Password_warning, "⚠ Password required"):
                valid = False
            elif password_data[0] != self.Password_entry.get():
                self.Password_warning.configure(text="⚠ Incorrect Password")
                valid = False

        # Terms Checkbox
        if not self.Accept_Terms.get():
            self.Submit_Btn_warning.configure(text="⚠ Must accept our Terms.")
            valid = False

        if valid:
            #this time is a bit different since we have an option that if it got activated it will insert a new file with a token
            #So we simply check first if the token column is here if not , do one, if yes insert a token (The token is randomly generated!)
            # Stay Logged Token
            if self.Stay_logged.get():
                columns = [column[1] for column in DB.fetchall("PRAGMA table_info(Users);")]

                if "token" not in columns:
                    DB.execute("ALTER TABLE Users ADD COLUMN token TEXT;")
                
                token = Side_Functions.generate_token()
                with open("User_Out_Data/auth_token.txt", "w") as f:
                    f.write(token)
                DB.execute("UPDATE Users SET token = ? WHERE Email = ?", (token, self.Email.get()))
            result = DB.fetchone("SELECT ID, Name, Activity, Body_Weight, Body_Height, Age FROM Users WHERE Email = ?", (self.Email.get(),))
            session = user_session(result) 
            save_session(*session) # => Saving the data in a json file, so we can access it at anytime!
            
            self.destroy()
            self.Access()

    def Access(self):
        #After we successfully logged in, We show this nice Window which is just a loading bar that take us to the Main Window!
        try:
            # if accessed this window for check if sure window then destroy it and if this true then we logged from the token, this we can take the token
            #and get the data from it and store it in the session.json file so we can access the data easily!
            self.Check_if_logged_window.destroy()
            result = DB.fetchone("SELECT ID, Name, Age, Body_Weight, Body_Height, Activity FROM Users WHERE token = ?", (self.token,))
            result = user_session(*result)
            save_session(result)
        except AttributeError:
            return None
        self.Access_Gained = ctk.CTkToplevel()
        self.Access_Gained.geometry("400x200")
        self.Access_Gained.title("Processing...")

        self.Bar = ctk.CTkProgressBar(self.Access_Gained, width=300, progress_color="green", corner_radius=6, height=30)
        self.Bar.pack(pady=50)
        self.Bar.set(0)
        self.Access_Gained.attributes("-topmost", True)        
        # Brings to front
        self.Loading_Simulation()

    def Loading_Simulation(self, value=0):
        #Nice bar which gets filled over time!
        if value <= 1:
            self.Bar.set(value)
            self.Access_Gained.after(100, lambda: self.Loading_Simulation(value + 0.02))
        else:
            #After the progress bar is done, we can show this nice label to let the user know that the main window is getting launched!
            Loading_Text = ctk.CTkLabel(self.Access_Gained, text="Entering Main Menu...", **Styles.label_styles["subtitle2"])
            Loading_Text.pack(pady=10)
            self.Access_Gained.after(2000, self.Access_Gained.destroy)
            try:
                Data_Load = load_session()
                try:
                    Access = DB.fetchone("SELECT Full_Logged FROM Users WHERE ID = ?", (Data_Load["ID"],))
                except sqlite3.OperationalError:
                    Access = None
                    if self.switch_screen:
                        self.switch_screen()
                if Access:
                    self.Logged_switch_screen()
                    
            except (TypeError, AttributeError) as e:
                print(f"[Handled Error] {e}")
                if self.switch_screen:
                    self.switch_screen()

    def Create_Login_Frame(self):
        # The login frame but before doing it we check if we are logged if not continue normally, If yes then see what the user wants first 
        #If not create the login frame if yes then continue to the main menu
        self.Check_if_Logged()
        Login_Label = ctk.CTkLabel(self, text="Login", width=147, height=58, **Styles.label_styles["title2"])
        Login_Label.place(x=293, y=20)

        Email_Label = ctk.CTkLabel(self, text="Email:", width=134, height=58, **Styles.label_styles["subtitle2"])
        Email_Label.place(x=185, y=80)

        self.Email_entry = ctk.CTkEntry(self, textvariable=self.Email, width=346, height=50, **Styles.entry_styles["default"])
        self.Email_entry.place(x=209, y=129)

        self.Email_warning = ctk.CTkLabel(self, width=300, height=24, text="", **Styles.label_styles["error_title"])
        self.Email_warning.place(x=209, y=185)

        Password_Label = ctk.CTkLabel(self, text="Password:", **Styles.label_styles["subtitle2"])
        Password_Label.place(x=205, y=211)

        self.Password_entry = ctk.CTkEntry(self, textvariable=self.Password, show="*", width=334, height=41, **Styles.entry_styles["default"])
        self.Password_entry.place(x=209, y=250)

        password_show_btn = ctk.CTkButton(
            self,
            text="👁",
            font=("Lato", 30, "bold"),
            width=48,
            height=50,
            fg_color="#000000",
            bg_color="#2B2B2B",
            border_color="#CCCCCC",
            corner_radius=5,
            hover_color="#FFE23D",
            command=lambda: self.Password_entry.configure(show="")
        )
        password_show_btn.place(x=543, y=245)

        self.Password_warning = ctk.CTkLabel(self, text="", width=300, height=24, **Styles.label_styles["error_title"])
        self.Password_warning.place(x=209, y=295)

        # Terms and Privacy Checkbox
        self.Terms_and_Privacy_Cb = ctk.CTkCheckBox(self, text="Accept our terms and conditions\nand privacy statement", 
                                                    variable=self.Accept_Terms, 
                                                    checkbox_height=40, 
                                                    checkbox_width=40, 
                                                    corner_radius=8,
                                                    font=("Lato", 20, "bold"),
                                                    text_color="#c4c364",
                                                    text_color_disabled="#E5FF00")
        self.Terms_and_Privacy_Cb.place(x=220, y=360)


        # Stay Logged In Checkbox
        self.Stay_Logged_Cb = ctk.CTkCheckBox(self, text="", variable=self.Stay_logged, checkbox_width=40, checkbox_height=40, corner_radius=8)
        self.Stay_Logged_Cb.place(x=220, y=420)

        Stay_Logged_Text = ctk.CTkLabel(self, width=142, height=24, text="Stay Logged In", **Styles.label_styles["subtitle"])
        Stay_Logged_Text.place(x=274, y=428)

        Submit_Btn = ctk.CTkButton(self, width=250, height=60, text="LOGIN", **Styles.button_styles["Big"], command=self.Submit) # +> Activates the submit function!
        Submit_Btn.place(x=233, y=500)

        self.Submit_Btn_warning = ctk.CTkLabel(self, text="", width=300, height=24, **Styles.label_styles["error_title"])
        self.Submit_Btn_warning.place(x=233, y=565)
class Report_Section(ctk.CTkFrame):
    def __init__(self, master):
        #Setting up the main vars!
        super().__init__(master)
        self.Username = ctk.StringVar()
        self.Report_Type = ctk.StringVar()
        self.Report_Message = ""
        self.Create_Report_Frame()
    def Submit(self):
        #Normal and easy this time!
        valid = True
        if not Side_Functions.check_empty(self.Username, self.Warning_User, "⚠ Must Enter Username"):
            valid = False
            
        if valid:
            self.Check_if_sure()    
    def Check_if_sure(self):
        #A normal check if sure window!
        self.Sure_Windows = ctk.CTkToplevel()
        self.Sure_Windows.geometry("400x250")
        self.Sure_Windows.title("Are you sure?")
        ctk.CTkLabel(self.Sure_Windows, text="Are you sure \nyou want to proceed?: ", **Styles.label_styles["subtitle2"]).pack(pady=10)
        ctk.CTkButton(self.Sure_Windows, text="Yes", **Styles.button_styles["Small"], command=lambda: self.Insert_Report()).pack(padx=10, pady=10)
        ctk.CTkButton(self.Sure_Windows, text="No", **Styles.button_styles["Small"], command= self.Sure_Windows.destroy).pack(padx=5, pady=5)
        self.Sure_Windows.attributes("-topmost", True)
    def Insert_Report(self):
        #Inserting the report !
        self.Sure_Windows.destroy()
        Cur_Feed_Repo.execute("INSERT INTO Users_Messages(Name, Type_Report, Report_Message) Values(?, ?, ?)", 
                            (self.Username.get(), self.Report_Type.get(), self.Report_Message.get("1.0", "end-1c")))
        Con_Feed_Repo.commit()
        
        #Thanking the user in a nice Top window 
        Thanks_Top = ctk.CTkToplevel()
        Thanks_Top.geometry("500x300")
        Thanks_Top.title("Thanks...")
        ctk.CTkLabel(Thanks_Top, text="Thanks for your time, \nyour problem will be investigated.", **Styles.label_styles["subtitle2"]).pack(pady=10)
        Thanks_Top.after(2000, Thanks_Top.destroy)
        Thanks_Top.attributes("-topmost", True)
        
    def Create_Report_Frame(self):
        #Creating the Report frame which is so simple
        Title_Label = ctk.CTkLabel(self, text="Report Section", **Styles.label_styles["title1"])
        Title_Label.place(x=231, y=20)
        
        Username_Label = ctk.CTkLabel(self, text="Username: ", **Styles.label_styles["subtitle2"])
        Username_Label.place(x=280, y=97)
        
        Username_Entry = ctk.CTkEntry(self, **Styles.entry_styles["default"], width=230, height=40, textvariable=self.Username)
        Username_Entry.place(x=280, y=130)
        
        self.Warning_User = ctk.CTkLabel(self, **Styles.label_styles["error_title"], text="")
        self.Warning_User.place(x=517, y=135)
        
        Report_Sel_Label = ctk.CTkLabel(self, **Styles.label_styles["subtitle2"], text="Type of Report?: ")
        Report_Sel_Label.place(x=278, y=189)
        
        Report_Sel_Cb = ctk.CTkComboBox(self, values=["Problem Signing In.",
                                                    "Not letting me in even tho I have Stay Logged on.",
                                                    "Not Correct Calculation.",
                                                    "Wrong Data and not updating.",
                                                    "The Program freezes When i click a button.",
                                                    "Other."],
                                            width=230,
                                            height=40,
                                            variable=self.Report_Type,
                                            state="readonly",
                                            border_color="#4A90E2",
                                            bg_color="#2B2B2B",
                                            dropdown_fg_color="#2B2B2B",
                                            dropdown_text_color="white",
                                            text_color="white",
                                            button_color="grey",
                                            font=("Lato", 20, "bold"),
                                            dropdown_font=("Lato", 20, "bold"))
        Report_Sel_Cb.place(x=280, y=222)
        Report_Sel_Cb.set("Problem Signing In.")
        
        Report_Label = ctk.CTkLabel(self, text="Text report message (optional): ", **Styles.label_styles["subtitle2"])
        Report_Label.place(x=218, y=280)
        
        self.Report_Message = ctk.CTkTextbox(self, **Styles.entry_styles["default"], width=410, height=200, )
        self.Report_Message.place(x=195, y=310)
        
        Submit_Button = ctk.CTkButton(self, **Styles.button_styles["Big"], 
                                    width=210, 
                                    height=50,
                                    text="Send",
                                    command=lambda: self.Submit()) # => Activating the submit function
        Submit_Button.place(x=290, y=530)