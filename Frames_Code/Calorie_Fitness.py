import os
import sys
from path_setup import get_data_path, add_frames_path
add_frames_path("Data_Side")
from db_connection import DBConnection # type: ignore
import customtkinter as ctk
import sqlite3
import Styles
import Side_Functions
import json
from PIL import Image
from User_session import load_session
#Importing the most needed Classes!
#Starting the part 2 from the project 
DB = DBConnection("Data_Side/Users_Data.db")
DB.execute("PRAGMA foreign_keys = ON;")
with open(get_data_path("GYM_Queries.sql"), "r") as file:
    sql_script = file.read()
    DB.executescript(sql_script)

class Program_setUp(ctk.CTkFrame):
    def __init__(self, master, switch_screen=None):
        #All in one this time but it work perfectly! 
        # Setting up the vars!
        super().__init__(master)
        self.switch_screen = switch_screen
        self.Diet_Goal = ctk.StringVar()
        self.target_weight = ctk.IntVar()
        self.gender = ctk.StringVar()
        self.Training_Days_Ava = ctk.StringVar()
        self.intensity_Level = ctk.StringVar()
        self.Days_Off_Activity = ctk.StringVar()
        self.Experience_Level = ctk.StringVar()
        self.Create_Details_Frame()
        
    def Submit(self):
        #Checking if everything is nicely here!
        valid = True

        if not Side_Functions.check_empty(self.Diet_Target_Entry, self.Submit_Button_warning, "⚠ Must Enter A Number"):
            valid = False
        elif int(self.Diet_Target_Entry.get()) < 0:
            valid = False
            self.Submit_Button_warning.configure(text="⚠ Negative Numbers \n aren't allowed.")
        if valid:
            self.Check_if_Sure()
            
    def Insert_Data(self):
        #Insert The data gotten from the user!
        self.Sure_Windows.destroy()
        Data_load = load_session()
        DB.execute("""INSERT INTO Program_Users(
            User_id,
            Gender,
            Diet_Goal,
            Target_Weight,
            Training_Days,
            Not_Active_Days,
            Intensity_Level,
            Experience
            ) VALUES(?, ?, ?, ?, ?, ?, ?, ?)""", 
            (Data_load["ID"], self.gender.get(), self.Diet_Goal.get(), self.target_weight.get(), self.Training_Days_Ava.get(),
            self.Days_Off_Activity.get(), self.intensity_Level.get(), self.Experience_Level.get()))
        #This one is a bit tricky but let me explain we are going to get the program choice which is True or False
        #Then depending on this it will give us the Option of doing the user program or not but because it was hard to put this function
        #In the main function i made it alone, I may fixed it later but all we need to know that this function returns True or False depending in what he chose
        
        choice = self.Program_Choice()
        Data = self.Program_Calc()
        #This Function returns every needed data , we will explain how we get it down!
        #return Pr_BMR, standard, Final_result, Program
        DB.execute("INSERT INTO Program_Data(User_id, BMR, Calories, TDEE, Program_Choice) VALUES(?, ?, ?, ?, ?)",
                    (Data_load["ID"], *Data, choice))    


        result = DB.fetchall("PRAGMA table_info(Users);")
        columns = [column[1] for column in result]

        if "Full_Logged" not in columns:
            DB.execute("ALTER TABLE Users ADD COLUMN Full_Logged TEXT;")
        DB.execute("UPDATE Users SET Full_Logged = ? WHERE ID = ?", (True ,Data_load["ID"]))

    def switch_page(self):
        #Not using the try/expect stuff because this function doesn't get activated expect when it is needed! 
        self.Program_Choice_Window.destroy()
        if self.switch_screen:
            self.switch_screen()
            
    def Check_if_Sure(self):
        self.Sure_Windows = ctk.CTkToplevel()
        self.Sure_Windows.geometry("400x250")
        self.Sure_Windows.title("Are you sure?")
        ctk.CTkLabel(self.Sure_Windows, text="Are you sure \nyou want to proceed?: ", **Styles.label_styles["subtitle2"]).pack(pady=10)
        ctk.CTkButton(self.Sure_Windows, text="Yes", **Styles.button_styles["Small"], command=lambda: self.Insert_Data()).pack(padx=10, pady=10)
        ctk.CTkButton(self.Sure_Windows, text="No", **Styles.button_styles["Small"], command= self.Sure_Windows.destroy).pack(padx=5, pady=5)
        self.Sure_Windows.attributes("-topmost", True)
    
    def Get_Activity(self):
        # This is a simple Function that loads the user data and get the activity rate (Digital Number)!
        Data_load = load_session()
        """_summary_
        Basal Metabolic Rate (BMR)", 
                                                    "Sedentary: little or no exercise",
                                                    "Light: exercise 1-3 times/week",
                                                    "Moderate: exercise 4-5 times/week",
                                                    "Active: daily exercise or intense exercise 3-4 times/week",
                                                    "Very Active: intense exercise 6-7 times/week",
                                                    "Extra Active: very intense exercise daily, or physical job
        """
        if Data_load["Activity"] == "Basal Metabolic Rate (BMR)":
            return None
        elif Data_load["Activity"] == "Sedentary: little or no exercise":
            return 1.2
        elif Data_load["Activity"] == "Light: exercise 1-3 times/week":
            return 1.375
        elif Data_load["Activity"] == "Moderate: exercise 4-5 times/week":
            return 1.55
        elif Data_load["Activity"] == "Active: daily exercise or intense exercise 3-4 times/week":
            return 1.65
        elif Data_load["Activity"] == "Very Active: intense exercise 6-7 times/week":
            return 1.725
        elif Data_load["Activity"] == "Extra Active: very intense exercise daily, or physical job":
            return 1.9
        else:
            print("Hmm, What in the actual Python is this?")
    def Program_Choice(self, choice=True):
            #This is here for getting the true/false value so i can make the program if true and not if false
            self.Program_Choice_Window = ctk.CTkToplevel()
            self.Program_Choice_Window.geometry("700x250")
            self.Program_Choice_Window.title("Program Choice")
            Exp_Message = ""
            if self.Experience_Level.get() == "Standard":
                Exp_Message = "You know well, \n Do you Wish That we do your Program?"
            elif self.Experience_Level.get() == "Beginner":
                Exp_Message = "You are a beginner, Don't Worry we can Help \n You Can click Yes if you want us to make you the Program"
            elif self.Experience_Level.get() == "PRO":
                Exp_Message = "You are a PRO,\nIf you want us to make your Program Click Yes!"
            elif self.Experience_Level.get() == "Know a bit":
                Exp_Message = "You know a bit,\nWell then if you need more help Click Yes"
                
            ctk.CTkLabel(self.Program_Choice_Window, text=Exp_Message, **Styles.label_styles["subtitle2"]).pack(pady=10)
            Choice = ctk.StringVar()
            Choice_Cb = ctk.CTkComboBox(self.Program_Choice_Window, variable=Choice, values=["Yes Give me the Program", "No Thanks I want to make my own"], **Styles.ComboBox["Box1"],
                                        width=500)
            Choice_Cb.pack()
            Choice_Cb.set("Yes Give me the Program")
            Button = ctk.CTkButton(self.Program_Choice_Window, text="Choose", **Styles.button_styles["Small"], command=lambda: self.switch_page())
            Button.pack(padx=10, pady=15)
            if Choice_Cb.get() == "Yes Give me the Program":
                choice = True
                return choice
            elif Choice_Cb.get() == "No Thanks I want to make my own":
                choice = False
                return choice

            self.Program_Choice_Window.attributes("-topmost", True)
            self.Program_Choice_Window.grab_set()
            self.Program_Choice_Window.wait_window()

    def Program_Calc(self):
        #This is a huge function that has three functions working to get the last result!
        Data_Load = load_session()
        Program_Data_load = DB.fetchone("SELECT Gender, Diet_Goal, Target_Weight, Training_Days, Not_Active_Days, Intensity_Level, Experience FROM Program_Users WHERE Name = ?", (Data_Load["name"],))
        Activity_Num = self.Get_Activity()
        def BMR_Calc():
            #BMR Formula depending on the Gender , a certain formula is applied and restored!
            #The get activity func is out because it doesn't make any since if it is here, It only returns a number that is needed for the formula nothing else!
            Pr_BMR = 0
            if Program_Data_load[0] == "Male":
                Pr_BMR += 10 * Data_Load["weight"] + 6.25 * Data_Load["height"] - 5 * Data_Load["age"] + 5
                return round(Pr_BMR)
            elif Program_Data_load[0] == "Female":
                Pr_BMR += 10 * Data_Load["weight"] + 6.25 * Data_Load["height"] - 5 * Data_Load["age"] - 161        
                return round(Pr_BMR)
        def TDEE_Calc():
            #TDEE Formula to get the actual calorie burning daily!, This is also needed for the diet plan!
            TDEE_Pr = 0
            Bmr = BMR_Calc()
            if Activity_Num:
                TDEE_Pr += Bmr * Activity_Num
                return round(TDEE_Pr)
            else:
                return Bmr
            
        def Calories_Table_Calc():
            #Depending on the goal, it will increase/decrease or stay the same!
            default = TDEE_Calc() 
            if self.Diet_Goal.get() == "Maintain My Weight":
                return default
            elif self.Diet_Goal.get() == "Lose Weight":
                standard = [default - 250, default - 500, default - 750]
                return standard
            elif self.Diet_Goal.get() == "Gain Weight":
                standard = [default + 250, default + 500, default + 1000]
                return standard
        BMR = BMR_Calc()
        TDEE = TDEE_Calc()
        CALORIES = Calories_Table_Calc()
        
        return BMR, json.dumps(CALORIES), TDEE # => Dumps some of them as a string because it is more than one value!
        
    def Create_Details_Frame(self):
        #Creating the Details Frame containing everything needed to get the needed Data!. 
        #After this should be the MainMenu!
        #bkg_Image = ctk.CTkImage(dark_image=Image.open("Window_Images/Black GYM Background.jpeg"), size=(1000, 700))
        
        #bg_label = ctk.CTkLabel(self, image=bkg_Image, text="")
        #bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)
        
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
        
        self.Diet_Target_Entry = ctk.CTkEntry(self, textvariable=self.target_weight, **Styles.entry_styles["default"], 
                                        width=128, height=50)
        self.Diet_Target_Entry.place(x=182, y=410)
        
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
                                    command=lambda: self.Submit()) # => Activating the Submit Func!
        Submit_Button.place(x=557, y=530)
        
        self.Submit_Button_warning = ctk.CTkLabel(self, text="", **Styles.label_styles["error_title"])
        self.Submit_Button_warning.place(x=826, y=546)