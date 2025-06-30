import customtkinter as ctk
import Styles
from tkinter import filedialog
import Side_Functions
import User_session as us
from PIL import Image
import sqlite3
import pandas as pd
import matplotlib as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import json
import datetime
from path_setup import get_data_path

Conn, Cur = Side_Functions.openData(get_data_path("Users_Data.db"))
mainMenu_Window = ctk.CTk()
mainMenu_Window.geometry("1000x600")
mainMenu_Window.title("Dashboard")
in_frame = ctk.CTkFrame(mainMenu_Window, width=768, height=520, border_color="white", border_width=2)
in_frame.place(x=220, y=70)
class tabView:
    def __init__(self):
        self.Data_load = us.load_session()
        self.allTab_buttons = {}
    
    def Error_Popup_Window(self, Label_Text, Button_Text):
        root = ctk.CTkToplevel()
        root.geometry("500x150")
        root.title("Error")
        ctk.CTkLabel(root, text=Label_Text, **Styles.label_styles["Menu_Labels2"]).pack()
        ctk.CTkButton(root, text=Button_Text, **Styles.button_styles["Small"], command=root.destroy).pack(pady=10)
        root.attributes("-topmost", True)
        
    def create_TabView(self):
        
        self.Tab_Btn = {
                    "Profile": {
                        "Icon_path_Active": ctk.CTkImage(dark_image=Image.open("Window_Images/Active_Pr.png"), size=(28, 28)),
                        "Icon_path": ctk.CTkImage(dark_image=Image.open("Window_Images/Default_Pr.png"), size=(28, 28)),
                        "style": "First",
                        "command": lambda: self.Open_Profile(),
                        "Default_color": "#FFAA4D",
                        "Active_color": "#C1733B"  
                    },
                    "Settings": {
                        "Icon_path_Active": ctk.CTkImage(dark_image=Image.open("Window_Images/Active_Sett.png"), size=(28, 28)),
                        "Icon_path": ctk.CTkImage(dark_image=Image.open("Window_Images/Default_Sett.png"), size=(28, 28)),
                        "style": "Second",
                        "command": lambda: self.Open_Settings(),
                        "Default_color": "#4A8AE8",
                        "Active_color": "#2F69B8" 
                    },
                    "Logout": {
                        "Icon_path_Active": ctk.CTkImage(dark_image=Image.open("Window_Images/logout.png"), size=(28, 28)),
                        "Icon_path": ctk.CTkImage(dark_image=Image.open("Window_Images/Default_logout.png"), size=(28, 28)),
                        "style": "Danger!",
                        "command": lambda: self.Check_if_sure(),
                        "Default_color": "#CF0808",
                        "Active_color": "#C70000" 
                    }
                }

        for i, (key, item) in enumerate(self.Tab_Btn.items()):
                b = ctk.CTkButton(self, text=f" {key}", width=150, height=50,
                            image=item["Icon_path"],
                            **Styles.button_styles[item["style"]],
                            compound="left",
                            command=item["command"])
                b.place(x=500 + i*170, y=11)
                b.bind("<Enter>", b.configure(cursor="hand2"))
                self.allTab_buttons[key] = b
    def Open_Profile(self, section="Profile"):
        Current_Email = Cur.execute("SELECT Email FROM Users WHERE ID = ?", (self.Data_load["ID"],)).fetchone()
        Email = ctk.StringVar()
        Name = ctk.StringVar()
        self.switch_toTab(section)
        Pr_Top = ctk.CTkToplevel()
        Pr_Top.geometry("300x450")
        Pr_Top.grid_columnconfigure((0, 1, 2), weight=1)
        def Change_Email():
            def Submit_Email():
                if Email.get() == "":
                    self.Error_Popup_Window("Please Enter an Email If you don't want,\n Close the Window", "Close")
                        
                elif Email.get() == Current_Email[0]:
                    self.Error_Popup_Window("Same Email!,\n Please Change it or Close the Window", "Close")
                        
                elif Side_Functions.suggest_email_domain(Email.get()) is not None:
                    self.Error_Popup_Window(Side_Functions.suggest_email_domain(Email.get()), "Close")
                    
                elif not "@" in list(Email.get()):
                        self.Error_Popup_Window("This is not an email!", "Close")
                else:
                    Email_label.configure(text=Side_Functions.mask_email(Email.get()))
                    Email_Top.destroy()
                        
            Email_Top = ctk.CTkToplevel()
            Email_Top.geometry("400x200")
            Email_Top.grid_columnconfigure((0, 1, 2), weight=1)
            ctk.CTkLabel(Email_Top, text="Enter the email that you want it:",
                        **Styles.label_styles["Menu_Labels2"]).grid(row=0, column=1, pady=10)
            ctk.CTkEntry(Email_Top, textvariable=Email,
                        width=250, height=30,
                        **Styles.entry_styles["default"]).grid(row=1, column=1, pady=5)
            ctk.CTkButton(Email_Top, text="Save",
                        width=150, height=50,
                        **Styles.button_styles["Quick"],
                        command=Submit_Email).grid(row=2, column=1, pady=10)
                
        def Change_Name():
            Names = Cur.execute("SELECT Name FROM Users").fetchall()
            Name_Top = ctk.CTkToplevel()
            Name_Top.geometry("400x200")
            Name_Top.title("Changing Name")
            Name_Top.grid_columnconfigure((0, 1, 2), weight=1)
            def Submit_Name():
                if Name.get() == "":
                    self.Error_Popup_Window("Please Enter an Name & If you don't want, Close the Window", "Close")
                elif Name.get() == self.Data_load["name"]:
                    self.Error_Popup_Window("Same Name!, Please Change it or Close the Window", "Close")
                elif len(Name.get()) > 32:
                    self.Error_Popup_Window("Long Name! Please Change it or Close the Window", "Close")
                elif len(Name.get()) < 5:
                    self.Error_Popup_Window("Too Short! Please Change it or Close the Window", "Close")
                elif Name.get() in Names:
                    Nums_random = Side_Functions.generate_random_num(2)
                    self.Error_Popup_Window(f"""Already Used Name, Please Changed or Try \n
                                                [{Name.get()}{Nums_random},
                                                {Name.get()}{Nums_random},
                                                {Name.get()}{Nums_random}]""",
                                                "Close")
                else:
                    Name_Top.destroy()      
                    username_label.configure(text=Name.get())
                        
            ctk.CTkLabel(Name_Top, text="Enter the Name that you want it:",
                        **Styles.label_styles["Menu_Labels2"]).grid(row=0, column=1, pady=10)
            ctk.CTkEntry(Name_Top, textvariable=Name,
                        width=200, height=50,
                        **Styles.entry_styles["default"]).grid(row=1, column=1, pady=5)
            ctk.CTkButton(Name_Top, text="Save",
                        width=75, height=50,
                        **Styles.button_styles["Quick"],
                        command=Submit_Name).grid(row=2, column=1, pady=10)
                
                
        def Save():
            Cur.execute("UPDATE Users SET Name = ?, Email = ? WHERE ID = ?",
                        (Name.get(), Email.get(), self.Data_load["ID"]))
            Conn.commit()
            self.Data_load["name"] = Name.get()
        def choose_image():
            file_path = filedialog.askopenfilename(
                title="Choose an image",
                filetypes=[("Image Files", "*.png *.jpg *.jpeg *.webp")]
                )
            if file_path:
                Circle_Image = Side_Functions.make_circle_image(file_path, size=(120, 120))
                ctk_img = ctk.CTkImage(light_image=Circle_Image, dark_image=Circle_Image, size=(120, 120))
                image_label.configure(image=ctk_img)
                image_label.image = ctk_img
                self.Data_load["Image"] = file_path
            
            #=============================[Title]==============================
        Pr_Pic = ctk.CTkImage(dark_image=Image.open(self.Data_load["Image"]), size=(28, 28))
        Pr_Title = ctk.CTkLabel(Pr_Top, text=" Profile", image=Pr_Pic, compound="left", **Styles.label_styles["Menu_title"])
        Pr_Title.grid(row=0, column=1, pady=(5, 20))
            #=============================[Circle Image]==============================
        No_Image_Circle = Side_Functions.make_circle_image("Window_Images/Test.png", size=(120, 120))
        No_Image = ctk.CTkImage(dark_image=No_Image_Circle, light_image=No_Image_Circle, size=(120, 120))
        image_label = ctk.CTkLabel(Pr_Top, text="", image=No_Image)
        image_label.grid(row=1, column=1, pady=1)
        info_frame = ctk.CTkFrame(Pr_Top, fg_color="transparent")
        info_frame.grid(row=2, column=1, pady=20)
        #=============================[User Details Frame]==============================
        Pencil_Image = ctk.CTkImage(dark_image=Image.open("Window_Images/Pencil.png"), light_image=Image.open("Window_Images/Pencil.png"), size=(25, 25))
        Username = self.Data_load["name"]
        username_label = ctk.CTkLabel(info_frame, text=Username, **Styles.label_styles["Menu_Labels2"])
        username_label.grid(row=0, column=0, padx=(0, 0))
        
        username_btn = ctk.CTkButton(info_frame, text="",image=Pencil_Image,
                                    width=32, height=32,
                                    **Styles.button_styles["Quick"],
                                    command=Change_Name)
        username_btn.grid(row=0, column=1)
        
        Current_Email = Side_Functions.mask_email(Cur.execute("SELECT Email FROM Users WHERE ID = ?",
                                        (self.Data_load["ID"],))
                                        .fetchone()[0])
        
        Email_label = ctk.CTkLabel(info_frame, text=Current_Email, **Styles.label_styles["Menu_Labels2"])
        Email_label.grid(row=1, column=0, padx=(0, 0), pady=10)
        
        Email_btn = ctk.CTkButton(info_frame, text="",image=Pencil_Image,
                                width=32, height=32, 
                                **Styles.button_styles["Quick"],
                                command=Change_Email)
        Email_btn.grid(row=1, column=1, pady=10)
        
        #=============================[Upload\Save Buttons]==============================
        Update_Image_img = ctk.CTkImage(dark_image=Image.open("Window_Images/Upload.png"), size=(28, 28))
        Update_Image_btn = ctk.CTkButton(Pr_Top, text="Upload Image",
                                        image=Update_Image_img, compound="left",
                                        width=50, height=25, 
                                        **Styles.button_styles["Second"], command=choose_image)
        Update_Image_btn.grid(row=3, column=1, pady=30)
        
        Save_btn = ctk.CTkButton(Pr_Top, text="Save",width=50, height=25, **Styles.button_styles["Second"],
                                command=lambda: Save)
        Save_btn.grid(row=4, column=1)
    def switch_toTab(self, section):
        for key, item in self.allTab_buttons.items():
            print(self.Tab_Btn[key]["Icon_path"])
            item.configure(image=self.Tab_Btn[key]["Icon_path"], fg_color=self.Tab_Btn[key]["Default_color"])
                
        self.allTab_buttons[section].configure(image=self.Tab_Btn[section]["Icon_path_Active"], 
                                            fg_color=self.Tab_Btn[section]["Active_color"]
                                            )
    def Open_Settings(self, section="Settings"):
        self.switch_toTab(section)
        Settings_Top = ctk.CTkToplevel()
        Settings_Top.geometry("550x400")
        ctk.CTkLabel(Settings_Top, text="Settings", **Styles.label_styles["Menu_title"]).place(x=200, y=8)

        # ===================== Labels Dictionary =====================
        Top_labels = {
            "Theme:": {
                "Image": ctk.CTkImage(dark_image=Image.open("Window_Images/Theme.png"), size=(28, 28)),
                "y": 48,
                "x": 13
            },
            "Dark Mode:": {
                "Image": ctk.CTkImage(dark_image=Image.open("Window_Images/Dark.png"), size=(28, 28)),
                "y": 87,
                "x": 13
            },
            "Font Size:": {
                "Image": ctk.CTkImage(dark_image=Image.open("Window_Images/FS.png"), size=(28, 28)),
                "y": 130,
                "x": 13
            },
            "Behavior:": {
                "Image": ctk.CTkImage(dark_image=Image.open("Window_Images/BH.png"), size=(28, 28)),
                "y": 180,
                "x": 13
            },
            "Enable Notifications:": {
                "Image": ctk.CTkImage(dark_image=Image.open("Window_Images/Not.png"), size=(28, 28)),
                "y": 215,
                "x": 10
            },
            "Data:": {
                "Image": ctk.CTkImage(dark_image=Image.open("Window_Images/Data.png"), size=(28, 28)),
                "y": 270,
                "x": 13
            },
            "Default Colors:": {
                "Image": ctk.CTkImage(dark_image=Image.open("Window_Images/Colors.png"), size=(28, 28)),
                "y": 87,
                "x": 265
            },
            "Font Type:": {
                "Image": ctk.CTkImage(dark_image=Image.open("Window_Images/FT.png"), size=(28, 28)),
                "y": 130,
                "x": 245
            }
        }

        def update_slider_value(value):
            slider_label.configure(text=f"Font Size: {int(value)}")

        for key, item in Top_labels.items():
            l = ctk.CTkLabel(Settings_Top, text=key, image=item["Image"], compound="left", **Styles.label_styles["Top_Labels"])
            l.place(x=item["x"], y=item["y"])

        Mode_Switch = ctk.CTkSwitch(Settings_Top, onvalue="dark", offvalue="light", **Styles.Switches["Switch1"])
        Mode_Switch.place(x=170, y=90)

        Cb_Colors = ctk.CTkComboBox(
            Settings_Top,
            width=90,
            height=20,
            values=["blue", "yellow", "red", "orange", "green", "pink"],
            **Styles.ComboBox["Box2"]
        )
        Cb_Colors.place(x=450, y=90)
        Cb_Colors.set("blue")

        Slider_FS = ctk.CTkSlider(
            Settings_Top,
            width=90,
            height=19,
            progress_color="#1A9FB1",
            number_of_steps=24,
            from_=16,
            to=40,
            command=update_slider_value
        )
        Slider_FS.place(x=145, y=138)

        slider_label = ctk.CTkLabel(Settings_Top, text="Font size: 0")
        slider_label.place(x=155, y=160)

        Cb_FT = ctk.CTkComboBox(
            Settings_Top,
            width=150,
            height=19,
            values=["Lato", "Segoe UI", "Arial", "Tahoma", "Lucida Sans Unicode", "Calibri"],
            **Styles.ComboBox["Box2"]
        )
        Cb_FT.place(x=390, y=133)
        Cb_FT.set("Lato")

        Notifications_Switch = ctk.CTkSwitch(
            Settings_Top,
            onvalue=True,
            offvalue=False,
            **Styles.Switches["Switch1"]
        )
        Notifications_Switch.place(x=255, y=218)

        Warn_Image = ctk.CTkImage(dark_image=Image.open("Window_Images/Warn.png"), size=(24, 24))
        ctk.CTkLabel(
            Settings_Top,
            text="Clear Data/History:",
            image=Warn_Image,
            compound="left",
            **Styles.label_styles["Top_Labels"]
        ).place(x=19, y=300)

        Data_Switch = ctk.CTkSwitch(
            Settings_Top,
            width=54,
            height=27,
            onvalue=True,
            offvalue=False,
            **Styles.Switches["Switch1"]
        )
        Data_Switch.place(x=235, y=305)

        Submit_Btn = ctk.CTkButton(
            Settings_Top,
            text="Save",
            **Styles.button_styles["Second"],
            command=lambda: Save_Settings(
                Mode_Switch.get(),
                Cb_Colors.get(),
                Slider_FS.get(),
                Cb_FT.get(),
                Notifications_Switch.get(),
                Data_Switch.get()
            )
        )
        Submit_Btn.place(x=215, y=350)

        def Save_Settings(
            Mode_Choice="dark",
            Default_Colors="blue",
            Font_Size=16,
            Font_Type="Lato",
            Notifications=False,
            Data_History=False
        ):
            Data = us.UserSettings(Mode_Choice, Default_Colors, Font_Size, Font_Type, Notifications, Data_History)
            us.save_settings(self.Data_load["ID"], *Data)
    def Check_if_sure(self):
            self.switch_toTab("Logout")
            Sure_Windows = ctk.CTkToplevel()
            Sure_Windows.geometry("400x250")
            Sure_Windows.title("Are you sure?")
            ctk.CTkLabel(Sure_Windows, text="Are you sure \nyou want to proceed?", 
                        **Styles.label_styles["subtitle2"]).pack(pady=10)
            ctk.CTkButton(Sure_Windows, text="Yes", **Styles.button_styles["Small"], 
                        command=lambda: self.cleanup_exit()).pack(padx=10, pady=10)
            ctk.CTkButton(Sure_Windows, text="No", **Styles.button_styles["Small"], 
                        command=Sure_Windows.destroy).pack(padx=5, pady=5)
            Sure_Windows.attributes("-topmost", True)
    def cleanup_exit(self):
        mainMenu_Window.destroy()
class sideBar:
    def __init__(self):
        self.Data_load = us.load_session()()
        self.allSidebar_buttons = {}
        
    def switch_frame(self, frame): 
        for widget in self.in_frame.winfo_children():
            if isinstance(widget, ctk.CTkFrame):
                widget.place_forget()
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        
    def Create_sidebar_Frame(self):
        Calories = Cur.execute("SELECT Calories FROM Program_Data WHERE User_id = ?", (self.Data_load["ID"],)).fetchone()[0]
        Diet_Goal = Cur.execute("SELECT Diet_Goal FROM Program_Users WHERE User_id = ?", (self.Data_load["ID"])).fetchone()[0]
        Actual_Burn_cal = Cur.execute("SELECT TDEE FROM Program_Users WHERE User_id = ?", (self.Data_load["ID"])).fetchone()[0]
        Main_Calories = json.loads(Calories)
        self.sideBar_Btn = {
                "My Plan": {
                    "Icon_path_Active": ctk.CTkImage(dark_image=Image.open("Window_Images/Active_PP.png"), size=(28, 28)),
                    "Icon_path": ctk.CTkImage(dark_image=Image.open("Window_Images/Default_PP.png"), size=(28, 28)),
                    "style": "Third",
                    "command": lambda: Create_myPlan_Frame(),
                    "Default_color": "#32C766",
                    "Active_color": "#28A957"  
                },
                "Calories": {
                    "Icon_path_Active": ctk.CTkImage(dark_image=Image.open("Window_Images/Active_Cal.png"), size=(28, 28)),
                    "Icon_path": ctk.CTkImage(dark_image=Image.open("Window_Images/Default_Cal.png"), size=(28, 28)),
                    "style": "First",
                    "command": lambda: Calories_Section(Main_Calories, Actual_Burn_cal, Diet_Goal),
                    "Default_color": "#FFAA4D",
                    "Active_color": "#C1733B" 
                },
                "Exercises": {
                    "Icon_path_Active": ctk.CTkImage(dark_image=Image.open("Window_Images/Active_Exe.png"), size=(28, 28)),
                    "Icon_path": ctk.CTkImage(dark_image=Image.open("Window_Images/Default_Exe.png"), size=(28, 28)),
                    "style": "Second",
                    "command": lambda: Create_Exercises_Frame(),
                    "Default_color": "#4A8AE8",
                    "Active_color": "#2F69B8" 
                },
                "Journey": {
                    "Icon_path_Active": ctk.CTkImage(dark_image=Image.open("Window_Images/Active_Jour.png"), size=(28, 28)),
                    "Icon_path": ctk.CTkImage(dark_image=Image.open("Window_Images/Default_Jour.png"), size=(28, 28)),
                    "style": "Fourth",
                    "command": lambda: Create_Journey_Frame(),
                    "Default_color": "#9FA8DA",
                    "Active_color": "#8894C7" 
                },
                "Rate us!": {
                    "Icon_path_Active": ctk.CTkImage(dark_image=Image.open("Window_Images/Active_Rate.png"), size=(28, 28)),
                    "Icon_path": ctk.CTkImage(dark_image=Image.open("Window_Images/Default_Rate.png"), size=(28, 28)),
                    "style": "Third",
                    "command": lambda: self.Open_Rate_us(),
                    "Default_color": "#32C766",
                    "Active_color": "#28A957" 
                }
            }

        for i, (key, item) in enumerate(self.sideBar_Btn.items()):
            btn = ctk.CTkButton(self, text=f" {key}", width=184, height=50,
                        image=item["Icon_path"],
                        **Styles.button_styles[item["style"]],
                        compound="left",
                        command=item["command"])
            if i == 4:
                btn.place(x=24, y=528)
            else:
                btn.place(x=24, y=110 + i*80)
            btn.bind("<Enter>", btn.configure(cursor="hand2"))
            self.allSidebar_buttons[key] = btn
            
    def switch_toSidebar(self, section):
        for key, item in self.allSidebar_buttons.items():
            print(self.sideBar_Btn[key]["Icon_path"])
            item.configure(image=self.sideBar_Btn[key]["Icon_path"], fg_color=self.sideBar_Btn[key]["Default_color"])
                
        self.allSidebar_buttons[section].configure(image=self.sideBar_Btn[section]["Icon_path_Active"], 
                                            fg_color=self.sideBar_Btn[section]["Active_color"]
                                            )
class Calories_Section:
    def __init__(self, mainCalories, actualCalories, dietGoal):
        self.Data_load = us.load_session()
        self.mainCalories = mainCalories
        self.actualCalories = actualCalories
        self.dietGoal = dietGoal
        self.Cal_Frame = ctk.CTkFrame(in_frame, border_color="white", border_width=2)
        
    def Error_Popup_Window(self, Label_Text, Button_Text):
        root = ctk.CTkToplevel()
        root.geometry("500x150")
        root.title("Error")
        ctk.CTkLabel(root, text=Label_Text, **Styles.label_styles["Menu_Labels2"]).pack()
        ctk.CTkButton(root, text=Button_Text, **Styles.button_styles["Small"], command=root.destroy).pack(pady=10)
        root.attributes("-topmost", True)
        
    def showPlanStarter(self):
        def chosen_planDataLoad(Plan, typeGoal):
            Current_Plan = us.UserPlan(Plan, typeGoal)
            us.save_Plan(*Current_Plan)
            for frame in self.Cal_Frame.winfo_children():
                frame.destroy()
            self.load_mainCalFrame()

            # ===============Testing
        check_results = us.load_user_plan(self.Data_load["ID"])
        if check_results:
            chosen_planDataLoad(check_results["Plan"], check_results["targetGoal"])
        else:
            return None
        
        notPlan = Diet_Goal = Cur.execute(
            "SELECT Diet_Goal FROM Program_Users WHERE User_id = ?",
            (self.Data_load["ID"],)
        ).fetchone()[0]
        ctk.CTkButton(
            self.Cal_Frame,
            text="Make my Own Plan",
            **Styles.button_styles["Quick"],
            command=lambda: chosen_planDataLoad(Plan="Plan1", typeGoal=notPlan)
        ).grid(row=0, column=0, sticky="nw")

        Calories = Cur.execute(
            "SELECT Calories FROM Program_Data WHERE User_id = ?",
            (self.Data_load["ID"],)
        ).fetchone()[0]
        Diet_Goal = Cur.execute(
            "SELECT Diet_Goal FROM Program_Users WHERE User_id = ?",
            (self.Data_load["ID"],)
        ).fetchone()[0]
        Actual_Burn_cal = Cur.execute(
            "SELECT TDEE FROM Program_Users WHERE User_id = ?",
            (self.Data_load["ID"],)
        ).fetchone()[0]
        Main_Calories = json.loads(Calories)

        for i, Needed_Calories in enumerate(Main_Calories):
            Plan_Frame = ctk.CTkFrame(
                self.Cal_Frame, width=175, height=400,
                border_color="#9FA8DA", border_width=2
            )
            Plan_Frame.grid(row=1, column=i, padx=10, pady=15, sticky="n")
            Plan_Frame.grid_columnconfigure(list(range(6)), weight=1)

            ctk.CTkLabel(
                Plan_Frame,
                text=f"Plan{i+1}",
                **Styles.label_styles["Menu_Labels_Tiny"]
            ).grid(row=0, column=0, pady=(10, 5))

            ctk.CTkLabel(
                Plan_Frame,
                text=f"Target Calories: {Needed_Calories}",
                **Styles.label_styles["Menu_Labels_Tiny"]
            ).grid(row=1, column=0)

            burn_label = ""
            cardio_label = ""
            note_label = ""
            rate_label = ""
            plan_id = f"Plan{i+1}"
            command_goal = ""

            if Diet_Goal == "Maintain My Weight":
                burn_label = "Target Burned Calories: 220"
                note_label = "Eat clean, healthy food and stick to your target calories"
                command_goal = "Maintain My Weight"

            elif Diet_Goal == "Lose Weight":
                Target_burn = Needed_Calories - Actual_Burn_cal
                burn_label = f"Target Burned Calories: {Target_burn - 15}"
                command_goal = "Lose Weight"

                if Target_burn <= 300:
                    note_label = "Burn calories through running, exercise—even walking!"
                    rate_label = "0.25 kg loss per week"
                    plan_id = "Plan1"

                elif Target_burn <= 750:
                    note_label = "It's going to be tough, but HIIT or similar workouts will help."
                    rate_label = "0.30 - 0.5 kg loss per week"
                    plan_id = "Plan2"

                else:
                    note_label = "This is an intense program—avoid doing it for more than two weeks straight."
                    rate_label = "0.75kg -- 1kg loss per week"
                    plan_id = "Plan3"

            elif Diet_Goal == "Gain Weight":
                Calories_Diff = Needed_Calories - Actual_Burn_cal
                cardio_label = "Cardio if wanted: 15 - 30 min cardio"
                command_goal = "Gain Weight"

                if Calories_Diff <= 300:
                    note_label = "Prioritize carbs and protein in your meals."
                    rate_label = "0.25 kg gain per week"
                    plan_id = "Plan1"

                elif Calories_Diff <= 750:
                    note_label = "Choose clean food sources and avoid overexertion."
                    rate_label = "0.30 - 0.5 kg gain per week"
                    plan_id = "Plan2"

                else:
                    note_label = "Expect both muscle and fat gain—check out our cutting plans afterward!"
                    rate_label = "0.75kg -- 1kg gain per week"
                    plan_id = "Plan3"

            if burn_label:
                ctk.CTkLabel(Plan_Frame, text=burn_label, **Styles.label_styles["Menu_Labels_Tiny"]).grid(row=2, column=0, pady=5)
            elif cardio_label:
                ctk.CTkLabel(Plan_Frame, text=cardio_label, **Styles.label_styles["Menu_Labels_Tiny"]).grid(row=2, column=0, pady=5)

            ctk.CTkLabel(
                Plan_Frame,
                text=f"Note: {note_label}",
                wraplength=160,
                height=50,
                **Styles.label_styles["Menu_Labels_Tiny"]
            ).grid(row=3, column=0, pady=5)

            if rate_label:
                ctk.CTkLabel(Plan_Frame, text=rate_label, **Styles.label_styles["Menu_Labels_Tiny"]).grid(row=4, column=0, pady=5)
            else:
                ctk.CTkLabel(Plan_Frame, text="", height=20).grid(row=4, column=0)

            ctk.CTkButton(
                Plan_Frame,
                text="Choose",
                width=110,
                height=35,
                **Styles.button_styles["Quick"],
                command=lambda plan=plan_id, goal=command_goal: chosen_planDataLoad(plan, goal)
            ).grid(row=5, column=0, pady=(10, 20))

    def load_mainCalFrame(self):
        listOfMeals = ["Breakfast", "Lunch", "Dinner", "Snacks"]
        Taken_Cal = ctk.IntVar(value=0)
        Remained_Cal = ctk.IntVar(value=0)
        canvas_size = 250
        circle_padding = 30

        canvas = ctk.CTkCanvas(
            self.Cal_Frame,
            width=canvas_size,
            height=canvas_size,
            bg="#242424",
            highlightthickness=0
        )
        canvas.grid(row=0, column=0, sticky="wn")

        canvas.create_oval(
            circle_padding,
            circle_padding,
            canvas_size - circle_padding,
            canvas_size - circle_padding,
            fill="#7965EC"
        )

        Calories = [2500, 2700, 3000]
        Plan_Data = {"Plan": "Plan1", "targetGoal": "Maintain My Weight"}

        for i in range(3):
            if Plan_Data["Plan"] == f"Plan{i+1}":
                    ctk.CTkLabel(
                        self.Cal_Frame,
                        text=f"Target Calories:\n {Calories[i]}",
                        bg_color="#7965EC",
                        **Styles.label_styles["Tiny_Labels"]
                    ).place(x=70, y=70)

                    Cal_Taken = ctk.CTkLabel(
                        self.Cal_Frame,
                        text=f"Taken Calories: \n{Taken_Cal.get()}",
                        bg_color="#7965EC",
                        **Styles.label_styles["Tiny_Labels"]
                    )
                    Cal_Taken.place(x=70, y=110)

                    Cal_remained = ctk.CTkLabel(
                        self.Cal_Frame,
                        text=f"Remaining Calories: \n{Remained_Cal.get()}",
                        bg_color="#7965EC",
                        **Styles.label_styles["Tiny_Labels2"]
                    )
                    Cal_remained.place(x=65, y=155)

        plus_image = ctk.CTkImage(dark_image=Image.open("Window_Images/plus.png"), size=(24, 24))
        mealSectionFrame = ctk.CTkFrame(self.Cal_Frame, width=364, height=456)
        mealSectionFrame.grid(row=0, column=2, pady=5)

        for i, Section in enumerate(listOfMeals):
            print("Placing:", Section, "at row", i)
            F = ctk.CTkFrame(mealSectionFrame, width=354, height=108)
            F.grid(row=i, column=0, pady=10, sticky="n")

            ctk.CTkLabel(F, text=Section, **Styles.label_styles["Menu_Labels"]).place(x=5, y=8)

            ctk.CTkButton(
                F,
                text="Show Details",
                **Styles.label_styles["Menu_Labels"],
                command=lambda section=Section: self.Open_mealSection(section, "Details")
            ).place(x=68, y=78)

            ctk.CTkButton(
                F,
                text=" Add Meal",
                image=plus_image,
                compound="left",
                **Styles.label_styles["Menu_Labels"],
                command=lambda section=Section: self.Open_mealSection(section, "New Meal")
            ).place(x=210, y=75)
    def Open_mealSection(self, section, Type):
        if Type == "Details":
            Details = us.loadMealData(self.Data_load["ID"], section)
            if Details:
                Top_Meal_Details = ctk.CTkToplevel()
                Top_Meal_Details.geometry("600x600")
                Top_Meal_Details.title(f"{section} Details.")
                ctk.CTkLabel(Top_Meal_Details, text=f"Data: {Details["Date"]}", **Styles.label_styles["Menu_Labels"]
                            ).grid(row=0, column=0, pady=5)
                ctk.CTkLabel(Top_Meal_Details, text=f"Type of Meal: {Details["mealType"]}", **Styles.label_styles["Menu_Labels"]
                            ).grid(row=1, column=0, pady=5)
                for i, food in enumerate(Details["foodNames"]):
                    ctk.CTkLabel(Top_Meal_Details, text=f"Meal: {food}", **Styles.label_styles["Menu_Labels"]
                                ).grid(row=2 + i, column=0, pady=3)
                ctk.CTkLabel(Top_Meal_Details, text=f"Total Kcal: {Details["Kcal"]}", **Styles.label_styles["Menu_Labels"]
                            ).place(x=300, y=500)
                ctk.CTkButton(Top_Meal_Details, text="Close", **Styles.button_styles["Quick"], command=Top_Meal_Details.destroy)
                
                Diagram_Data = pd.read_sql_query(
                "SELECT Proteins, Carbs, Fats FROM Meal WHERE Section = ? AND User_id = ?",
                con=Conn,
                params=(section, self.Data_load["ID"])
                )
                Totals = Diagram_Data.sum()
                Labels = ["Protein", "Carbs", "Fats"]
                values = [Totals["Protein"], Totals["Carbs"], Totals["Fats"]]
                
                fig, ax = plt.subplots(figsize=(4, 4), dpi=100)
                ax.figure(figsize=(5, 5))
                ax.pie(values, labels=Labels, autopct="%1.1f%%", startangle=90)
                ax.set_title(f"Macro Split for section {section}")
                ax.axis("equal")
                
                chart = FigureCanvasTkAgg(fig, master=Top_Meal_Details)
                chart.draw()
                chart.get_tk_widget().grid(row=0, column=1, pady=10)
            else:
                self.Error_Popup_Window("No Data Found, Try To add Some", "Close")

        elif Type == "New Meal":
            self.openNewMeals(section)
            
    def openNewMeals(self, section):
        Search_Query = ctk.StringVar(value="Chicken")
        self.Total_Kcal = ctk.IntVar(value=0)
        self.Total_Protein = ctk.IntVar(value=0)
        self.Total_Carbs = ctk.IntVar(value=0)
        self.Total_Fats = ctk.IntVar(value=0)
        all_Meals = ctk.StringVar(value="No Meals Added")
        for widget in self.Cal_Frame:
            if not isinstance(widget, ctk.CTkCanvas):
                widget.destroy()
                
        ctk.CTkLabel(self.Cal_Frame, text=f"Meal: {section}").grid(row=0, column=0, sticky="n")
        self.Now_Made_Frame = ctk.CTkFrame(self.Cal_Frame,
                                        width=369,
                                        height=128,
                                        border_color="white",
                                        border_width=2).grid(row=0, column=1, pady=10)
        
        ctk.CTkLabel(self.Now_Made_Frame, text=f"Your Meal: {section}",**Styles.label_styles["Menu_Labels"]).grid(row=0, column=0, pady=3)
        
        ctk.CTkLabel(self.Now_Made_Frame, text=f"Total Kcal: {self.Total_Kcal.get()}", **Styles.label_styles["Menu_Labels"]
                    ).grid(row=0, column=1, pady=3)
        all_Meals.set(Cur.execute("SELECT Meal FROM Meals WHERE User_id =  ? AND Section = ?", (self.Data_load["ID"], section)).fetchall())
        ctk.CTkLabel(self.Now_Made_Frame, text=all_Meals.get(), **Styles.label_styles["Menu_Labels"]).grid(row=1, column=0, pady=5)
        
        ctk.CTkButton(self.Cal_Frame, text="Add", width=110, height=40, **Styles.button_styles["Quick"],
                    command=addMeal).grid(row=1, column=1, pady=10)
            
        edit_btn = ctk.CTkButton(self.Cal_Frame, text="Edit", width=110, height=40, **Styles.button_styles["Quick"], state="disabled",
                    command=editMeal)
        edit_btn.grid(row=1, column=2, pady=10)
        
        rem_btn = ctk.CTkButton(self.Cal_Frame, text="Remove", width=110, height=40, **Styles.button_styles["Quick"], state="disabled",
                    command=removeMealTopLoad)
        rem_btn.grid(row=1, column=3, pady=10)
        
        if all_Meals.get() != "No Meals Added" or all_Meals.get() != None:
            edit_btn.configure(state="normal")
            rem_btn.configure(state="normal")
            
        def addMeal():
            def get_search(Results):
                Results = Side_Functions.search_foods(Search_Query.get())
            Search_Results = None
            ctk.CTkEntry(self.Cal_Frame,
                        textvariable=Search_Query, 
                        width=250, height=39,
                        **Styles.entry_styles["Query"]
                        ).grid(row=0, column=0, pady=5)
            
            ctk.CTkButton(self.Cal_Frame, width=30, height=30, image="", compound="", **Styles.label_styles["Quick"],
                        command=lambda: get_search(Search_Results))
            
            Query_Frame_Shown = ctk.CTkFrame(self.Cal_Frame, width=300, height=385).grid(row=1, column=0, pady=10)
            
            for Item in Search_Results:
                for i, (key, value) in enumerate(Item.items()):
                    ctk.CTkLabel(Query_Frame_Shown, text=key, wraplength=100, **Styles.label_styles["Menu_Labels"]
                                ).grid(row=i, column=0, pady=5)
                    
                    ctk.CTkLabel(Query_Frame_Shown, text=f"ID: {value}", **Styles.label_styles["Menu_Labels_Tiny"]
                                ).grid(row=i, column=1, sticky="ne")
                    
                    ctk.CTkButton(Query_Frame_Shown, text="Choose", **Styles.button_styles["Quick"],
                                command=lambda: self.showTopDetails(key, section)).grid(row=i+1, column=1, pady=5)
                    
        def removeMealTopLoad():
            def deleteTheMealData(meal_section):
                Cur.execute("DELETE FROM Meals WHERE User_id = ? AND Section = ?", (self.Data_load["ID"], meal_section))
                Conn.commit()
            warnTop = ctk.CTkToplevel()
            warnTop.title("Removing meal")
            warnTop.geometry("500x5000")
            ctk.CTkLabel(warnTop, text="Are you sure you want to delete the whole meal?",
                        **Styles.label_styles["Menu_labels"]).pack(pady=10)
            
            ctk.CTkButton(warnTop, text="Yes, I am sure", **Styles.button_styles["Second"],
                        command=lambda: [deleteTheMealData(section), warnTop.destroy()]).pack(pady=10)
            
            ctk.CTkButton(warnTop, text="No, Thanks", **Styles.button_styles["Second"], command= warnTop.destroy).pack(pady=10)
        def editMeal():
            editTop = ctk.CTkToplevel()
            editTop.geometry("600x600")
            editTop.title(f"{section} Edit")
            ctk.CTkLabel(editTop, text=all_Meals.get(), **Styles.label_styles["Menu_Labels"]).pack(pady=5)
            
            Diagram_Data = pd.read_sql_query(
            "SELECT Proteins, Carbs, Fats FROM Meal WHERE Section = ? AND User_id = ?",
            con=Conn,
            params=(section, self.Data_load["ID"])
            )
            Totals = Diagram_Data.sum()
            Labels = ["Protein", "Carbs", "Fats"]
            values = [Totals["Protein"], Totals["Carbs"], Totals["Fats"]]
            
            fig, ax = plt.subplots(figsize=(4, 4), dpi=100)
            ax.figure(figsize=(5, 5))
            ax.pie(values, labels=Labels, autopct="%1.1f%%", startangle=90)
            ax.set_title(f"Macro Split for section {section}")
            ax.axis("equal")
            
            chart = FigureCanvasTkAgg(fig, master=editTop)
            chart.get_tk_widget().pack(pady=5,  padx=(0 , 10))
            ctk.CTkLabel(editTop, text="Still Working on editing the meal itself, For now you can try to add and remove",
                        **Styles.label_styles["Menu_Labels"]).pack()
            ctk.CTkButton(editTop, text="Add", **Styles.button_styles["Quick"],
                        command=lambda: [addMeal(), editTop.destroy()]).pack(pady=10)
    def showTopDetails(self, foodName, section):
        Kcal = ctk.StringVar(value="")
        Proteins = ctk.StringVar(value="")
        Carbs = ctk.StringVar(value="")
        Fats = ctk.StringVar(value="")
        
        chosen_foodTop = ctk.CTkToplevel()
        chosen_foodTop.geometry("500x600")
        chosen_foodTop.title(f"Food: {foodName}")
        chosen_foodTop.grid_columnconfigure((0, 1, 2), weight=1)
        vcmd = chosen_foodTop.register(Side_Functions.onlyDigits)
        
        ctk.CTkLabel(chosen_foodTop, text=foodName, **Styles.label_styles["Menu_Labels"]).grid(row=0, column=1, pady=5)
        
        grams = ctk.IntVar(value=100)
        entry = ctk.CTkEntry(chosen_foodTop, textvariable=grams, **Styles.entry_styles["Query"])
        
        entry._entry.configure(validate="key", validatecommand=(vcmd, "%S"))
        entry.grid(row=5, column=1, pady=3)
        
        allResults = Side_Functions.Get_Malnutrition(foodName, grams)

        Kcal.set(allResults["Calories"])
        Proteins.set(allResults["Protein"])
        Carbs.set(allResults["Carbs"])
        Fats.set(allResults["Fats"])
        
        ctk.CTkLabel(chosen_foodTop, text=f"Calories: {Kcal.get()}", **Styles.label_styles["Menu_Labels"]).grid(row=1, column=0, pady=5)
        
        ctk.CTkLabel(chosen_foodTop, text=f"Protein: {Proteins.get()}", **Styles.label_styles["Menu_Labels"]).grid(row=2, column=0, pady=5)
        
        ctk.CTkLabel(chosen_foodTop, text=f"Carbs: {Carbs.get()}", **Styles.label_styles["Menu_Labels"]).grid(row=3, column=0, pady=5)
        
        ctk.CTkLabel(chosen_foodTop, text=f"Fats: {Fats.get()}", **Styles.label_styles["Menu_Labels"]).grid(row=4, column=0, pady=5)
        
        ctk.CTkButton(chosen_foodTop, text="Save", **Styles.button_styles["Quick"], command=submit_entry).grid(row=6, column=1)
        
        def submit_entry():
            if grams == 0:
                self.Error_Popup_Window("Enter a number!", "Close")
            elif grams < 0:
                self.Error_Popup_Window("Enter a positive number!", "Close")
            else:
                Final = us.UserMealData(datetime.date.today(), section, foodName, grams, Kcal.get())
                us.saveDataMeal(self.Data_load["ID"], section, *Final)
                self.Total_Kcal.set(Kcal.get())
                self.Total_Protein.set(Proteins.get())
                self.Total_Carbs.set(Carbs.get())
                self.Total_Fats.set(Fats.get())
                Cur.execute("INSERT INTO Meals(User_id, Date, Section, Proteins, Carbs, Fats, Kcal) VALUES(?, ?, ?, ?, ?, ?, ?)",(
                    self.Data_load["ID"],
                    datetime.date.today(),
                    section,
                    foodName,
                    self.Total_Protein,
                    self.Total_Carbs,
                    self.Total_Fats,
                    self.Total_Kcal
                ))
                Conn.commit()