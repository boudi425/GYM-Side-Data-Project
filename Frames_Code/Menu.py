import customtkinter as ctk
import Styles
from tkinter import filedialog
import Side_Functions
from User_session import load_session, save_settings, load_user_Settings, user_session, UserSettings, UserPlan, save_Plan, load_user_plan
from PIL import Image
import sqlite3
import pandas as pd
import matplotlib as plt
import json

from path_setup import get_data_path

Conn, Cur = Side_Functions.openData(get_data_path("Users_Data.db"))

class mainMenu(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.allTab_buttons = {}
        self.allSidebar_buttons = {}
        self.Create_mainMenu_Frame()
        
    def Error_Popup_Window(self, Label_Text, Button_Text):
        root = ctk.CTkToplevel()
        root.geometry("500x150")
        root.title("Error")
        ctk.CTkLabel(root, text=Label_Text, **Styles.label_styles["Menu_Labels2"]).pack()
        ctk.CTkButton(root, text=Button_Text, **Styles.button_styles["Small"], command=root.destroy).pack(pady=10)
        root.attributes("-topmost", True)
        
    def load_settings(self):
        Data_load = load_session()
        Sett_Load = load_user_Settings(Data_load["ID"])
        ctk.set_appearance_mode(Sett_Load["theme"])
        ctk.set_default_color_theme(Sett_Load["color"])
        self.Font_Style = (Sett_Load["font_type"], Sett_Load["font_size"], "bold")
        self.Data_His = True
        self.Notifications = True
    def Create_mainMenu_Frame(self):
        ctk.CTkLabel(self, text="BLACK GYM Main Menu", **Styles.label_styles["Menu_title"]).place(x=10, y=12)
        self.in_frame = ctk.CTkFrame(self, width=768, height=520, border_color="white", border_width=2)
        self.in_frame.place(x=220, y=70)
        welcome_text = "\tWelcome to the BLACK GYM\n \taccess any feature just click a button!\n \tWe will be happy to hear your opinion Through the rate us!"
        ctk.CTkLabel(self.in_frame, text=welcome_text, **Styles.label_styles["Menu_Labels"]).place(x=85, y=65)
        self.Create_Tab_Frame()
        self.Create_sidebar_Frame()
    def switch_to(self, section):
        pass
    def switch_frame(self, frame): 
        for widget in self.in_frame.winfo_children():
            if isinstance(widget, ctk.CTkFrame):
                widget.place_forget()
        frame.place(relx=0, rely=0, relwidth=1, relheight=1)
    def Create_Tab_Frame(self):
        self.Tab_Btn = {
                "Profile": {
                    "Icon_path_Active": ctk.CTkImage(dark_image=Image.open("Window_Images/Active_Pr.png"), size=(28, 28)),
                    "Icon_path": ctk.CTkImage(dark_image=Image.open("Window_Images/Default_Pr.png"), size=(28, 28)),
                    "style": "First",
                    "command": lambda: Open_Profile(),
                    "Default_color": "#FFAA4D",
                    "Active_color": "#C1733B"  
                },
                "Settings": {
                    "Icon_path_Active": ctk.CTkImage(dark_image=Image.open("Window_Images/Active_Sett.png"), size=(28, 28)),
                    "Icon_path": ctk.CTkImage(dark_image=Image.open("Window_Images/Default_Sett.png"), size=(28, 28)),
                    "style": "Second",
                    "command": lambda: Open_Settings(),
                    "Default_color": "#4A8AE8",
                    "Active_color": "#2F69B8" 
                },
                "Logout": {
                    "Icon_path_Active": ctk.CTkImage(dark_image=Image.open("Window_Images/logout.png"), size=(28, 28)),
                    "Icon_path": ctk.CTkImage(dark_image=Image.open("Window_Images/Default_logout.png"), size=(28, 28)),
                    "style": "Danger!",
                    "command": lambda: Check_if_sure(),
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
            
        def Open_Profile(section="Profile"):
            Data_load = load_session()
            Current_Email = Cur.execute("SELECT Email FROM Users WHERE ID = ?", (Data_load["ID"],)).fetchone()
            Email = ctk.StringVar()
            Name = ctk.StringVar()
            switch_toTab(section)
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
                    elif Name.get() == Data_load["name"]:
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
                            (Name.get(), Email.get(), Data_load["ID"]))
                Conn.commit()
                Data_load["name"] = Name.get()
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
                    Data_load["Image"] = file_path
            
            #=============================[Title]==============================
            Pr_Pic = ctk.CTkImage(dark_image=Image.open(Data_load["Image"]), size=(28, 28))
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
            Username = Data_load["name"]
            username_label = ctk.CTkLabel(info_frame, text=Username, **Styles.label_styles["Menu_Labels2"])
            username_label.grid(row=0, column=0, padx=(0, 0))
            
            username_btn = ctk.CTkButton(info_frame, text="",image=Pencil_Image,
                                        width=32, height=32,
                                        **Styles.button_styles["Quick"],
                                        command=Change_Name)
            username_btn.grid(row=0, column=1)
            
            Current_Email = Side_Functions.mask_email(Cur.execute("SELECT Email FROM Users WHERE ID = ?",
                                            (Data_load["ID"],))
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
            
        def Open_Settings(section="Settings"):
            switch_toTab(section)
            Settings_Top = ctk.CTkToplevel()
            Settings_Top.geometry("550x400")
            ctk.CTkLabel(Settings_Top, text="Settings", **Styles.label_styles["Menu_title"]).place(x=200, y=8)
            #=================================================================
            def update_slider_value(value):
                slider_label.configure(text=f"Font Size: {int(value)}")
            for key, item in Top_labels.items():
                l = ctk.CTkLabel(Settings_Top, text=key, image=item["Image"], compound="left", **Styles.label_styles["Top_Labels"])
                l.place(x=item["x"], y=item["y"])
            #=================================================================
            
            Top_labels = {
                " Theme:": {
                    "Image": ctk.CTkImage(dark_image=Image.open("Window_Images/Theme.png"), size=(28,28)),
                    "y": 48,
                    "x": 13
                },
                " Dark Mode:": {
                    "Image": ctk.CTkImage(dark_image=Image.open("Window_Images/Dark.png"), size=(28,28)),
                    "y": 87,
                    "x": 13
                },
                " Font Size:": {
                    "Image": ctk.CTkImage(dark_image=Image.open("Window_Images/FS.png"), size=(28,28)),
                    "y": 130,
                    "x": 13
                },
                " Behavior:": {
                    "Image": ctk.CTkImage(dark_image=Image.open("Window_Images/BH.png"), size=(28,28)),
                    "y": 180,
                    "x": 13
                }, 
                " Enable Notifications:": {
                    "Image": ctk.CTkImage(dark_image=Image.open("Window_Images/Not.png"), size=(28,28)),
                    "y": 215,
                    "x": 10
                },
                " Data:": {
                    "Image": ctk.CTkImage(dark_image=Image.open("Window_Images/Data.png"), size=(28,28)),
                    "y": 270,
                    "x": 13
                },
                " Default Colors:": {
                    "Image": ctk.CTkImage(dark_image=Image.open("Window_Images/Colors.png"), size=(28,28)),
                    "y": 87,
                    "x": 265
                }, 
                " Font Type:": {
                    "Image": ctk.CTkImage(dark_image=Image.open("Window_Images/FT.png"), size=(28,28)),
                    "y": 130,
                    "x": 245
                }
            }
            
            Mode_Switch = ctk.CTkSwitch(Settings_Top,
                                        onvalue="dark", offvalue="light", **Styles.Switches["Switch1"])
            Mode_Switch.place(x=170, y=90)
            
            Cb_Colors = ctk.CTkComboBox(Settings_Top,
                                        width=90, height=20, 
                                        values=["blue", "yellow", "red", "orange", "green", "pink"], **Styles.ComboBox["Box2"])
            Cb_Colors.place(x=450, y=90)
            Cb_Colors.set("blue")
            
            Slider_FS = ctk.CTkSlider(Settings_Top, width=90, height=19, progress_color="#1A9FB1", 
                                    number_of_steps=24, from_=16, to=40,
                                    command=update_slider_value)
            Slider_FS.place(x=145, y=138)
            slider_label = ctk.CTkLabel(Settings_Top, text="Font size: 0")
            slider_label.place(x=155, y=160)
            
            Cb_FT = ctk.CTkComboBox(Settings_Top, 
                                    width=150, height=19, **Styles.ComboBox["Box2"],
                                    values=["Lato", "Segoe UI", "Arial", "Tahoma", "Lucida Sans Unicode", "Calibri"])
            Cb_FT.place(x=390, y=133)
            Cb_FT.set("Lato")
            
            Notifications_Switch = ctk.CTkSwitch(Settings_Top, **Styles.Switches["Switch1"], onvalue=True, offvalue=False)
            Notifications_Switch.place(x=255, y=218)
            
            Warn_Image = ctk.CTkImage(dark_image=Image.open("Window_Images/Warn.png"), size=(24, 24))
            ctk.CTkLabel(Settings_Top, text="Clear Data/History:" ,
                        image=Warn_Image, 
                        compound="left", **Styles.label_styles["Top_Labels"]).place(x=19, y=300)
            
            Data_Switch = ctk.CTkSwitch(Settings_Top, width=54, height=27, onvalue=True, offvalue=False, **Styles.Switches["Switch1"])
            Data_Switch.place(x=235, y=305)

            
            Submit_Btn = ctk.CTkButton(Settings_Top, text="Save", **Styles.button_styles["Second"], 
                                    command=lambda: Save_Settings(Mode_Switch.get(), 
                                                                Cb_Colors.get(), 
                                                                Slider_FS.get(),
                                                                Cb_FT.get(), 
                                                                Notifications_Switch.get(),
                                                                Data_Switch.get())).place(x=215, y=350)
            
            def Save_Settings(Mode_Choice="dark", 
                            Default_Colors="blue", 
                            Font_Size=16, 
                            Font_Type="Lato", 
                            Notifications=False, Data_History=False):
                Data = UserSettings(Mode_Choice, Default_Colors, Font_Size, Font_Type, Notifications, Data_History)
                save_settings("Boudi425", *Data)
        def switch_toTab(section):
            for key, item in self.allTab_buttons.items():
                print(self.Tab_Btn[key]["Icon_path"])
                item.configure(image=self.Tab_Btn[key]["Icon_path"], fg_color=self.Tab_Btn[key]["Default_color"])
                
            self.allTab_buttons[section].configure(image=self.Tab_Btn[section]["Icon_path_Active"], 
                                                fg_color=self.Tab_Btn[section]["Active_color"]
                                                )
        def Check_if_sure():
            switch_toTab("Logout")
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
    def Create_sidebar_Frame(self):
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
                    "command": lambda: Create_Calories_Frame(),
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
                    "command": lambda: Open_Rate_us(),
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
            
        def switch_toSidebar(section):
            for key, item in self.allSidebar_buttons.items():
                print(self.sideBar_Btn[key]["Icon_path"])
                item.configure(image=self.sideBar_Btn[key]["Icon_path"], fg_color=self.sideBar_Btn[key]["Default_color"])
                
            self.allSidebar_buttons[section].configure(image=self.sideBar_Btn[section]["Icon_path_Active"], 
                                                fg_color=self.sideBar_Btn[section]["Active_color"]
                                                )
        #========================================================================================================
        def Create_Calories_Frame(section="Calories"):
            Data_load = load_session()
            switch_toSidebar(section)
            Cal_Frame = ctk.CTkFrame(self.in_frame, border_color="white", border_width=2)
            self.switch_frame(Cal_Frame)
            Cal_Frame.grid_columnconfigure((0, 1, 2), weight=1)
            Cal_mainImage = ctk.CTkImage(dark_image=Image.open("Window_Images/Main_Cal.png"), size=(40, 40))
            ctk.CTkLabel(Cal_Frame, text=" Calorie Section", image=Cal_mainImage, compound="left",
                        **Styles.label_styles["Menu_subtitle"]).grid(row=0, column=1, pady=10)
            #===========================================================================================================
            
            def Plan_starter():
                def chosen_planDataLoad(Plan, typeGoal):
                    Current_Plan = UserPlan(Plan, typeGoal)
                    save_Plan(*Current_Plan)
                    for frame in Cal_Frame.winfo_children():
                        frame.destroy()
                    load_mainCalFrame()
                #===============Testing
                ctk.CTkButton(Cal_Frame, text="Make my Own Plan", **Styles.button_styles["Quick"],
                        command=lambda: chosen_planDataLoad(None, typeGoal="Nothing"))
                Calories = Cur.execute("SELECT Calories FROM Program_Data WHERE User_id = ?", (Data_load["ID"],)).fetchone()[0]
                Diet_Goal = Cur.execute("SELECT Diet_Goal FROM Program_Users WHERE User_id = ?", (Data_load["ID"])).fetchone()[0]
                Actual_Burn_cal = Cur.execute("SELECT TDEE FROM Program_Users WHERE User_id = ?", (Data_load["ID"])).fetchone()[0]
                Main_Calories = json.loads(Calories)
                
                for i, Needed_Calories in enumerate(Main_Calories):
                    Plan_Frame = ctk.CTkFrame(Cal_Frame, width=175, height=400, border_color="#9FA8DA", border_width=2)
                    Plan_Frame.grid(row=1, column=i, padx=10, pady=15, sticky="n")
                    Plan_Frame.grid_columnconfigure(list(range(6)), weight=1)
                    
                    ctk.CTkLabel(Plan_Frame, text=f"Plan{i+1}", **Styles.label_styles["Menu_Labels_Tiny"]).grid(row=0, column=0, pady=(10, 5))
                    ctk.CTkLabel(Plan_Frame, text=f"Target Calories: {Needed_Calories}", **Styles.label_styles["Menu_Labels_Tiny"]).grid(row=1, column=0)
                    
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
                        ctk.CTkLabel(Plan_Frame, text="", height=20).grid(row=4, column=0)  # Spacer
                    ctk.CTkButton(
                        Plan_Frame,
                        text="Choose",
                        width=110,
                        height=35,
                        **Styles.button_styles["Quick"],
                        command=lambda plan=plan_id, goal=command_goal: chosen_planDataLoad(plan, goal)
                    ).grid(row=5, column=0, pady=(10, 20))
            #===============================================================================================================
            
            def load_mainCalFrame():
                def Open_mealSection(Section):
                    pass
                listOfMeals = ["Breakfast", "Lunch", "Dinner", "Snacks"]
                self.Taken_Cal = ctk.IntVar()
                self.Remained_Cal = ctk.IntVar()
                canvas = ctk.CTkCanvas(Cal_Frame, width=200, height=200, bg="White", highlightthickness=0)
                canvas.grid(row=0, column=0, pady=15, padx=10)
                canvas.create_oval(20, 20, 130, 130, fill="grey")
                results = Cur.execute("SELECT Calories FROM Program_Data WHERE ID = ?", (Data_load["ID"])).fetchone()[0]
                Calories = json.loads(results) 
                Plan_Data = load_user_plan()
                for i in range(3):
                    if Plan_Data["Plan"] == f"Plan{i+1}":
                        if Plan_Data["targetGoal"] == "Maintain My Weight":
                            ctk.CTkLabel(Cal_Frame, text=f"Target Calories:\n {Calories[0]}"
                                        , **Styles.label_styles["Tiny_Labels"]).place(x=100, y=125)
                            Cal_Taken = ctk.CTkLabel(Cal_Frame, text=f"Taken Calories: \n{self.Taken_Cal}",
                                                    **Styles.label_styles["Tiny_Labels"])
                            Cal_Taken.place(x=100, y=150)
                            self.Taken_Cal.set(0)
                            Cal_remained = ctk.CTkLabel(Cal_Frame, text=f"Remaining Calories: \n{self.Remained_Cal}",
                                                    **Styles.label_styles["Tiny_Labels"])
                            Cal_remained.place(x=100, y=175)
                            self.Remained_Cal.set(Calories[0])
                        elif Plan_Data["targetGoal"] == "Lose Weight":
                            ctk.CTkLabel(Cal_Frame, text=f"Target Calories:\n {Calories[0]}"
                                        , **Styles.label_styles["Tiny_Labels"]).place(x=100, y=125)
                            Cal_Taken = ctk.CTkLabel(Cal_Frame, text=f"Taken Calories: \n{self.Taken_Cal}",
                                                    **Styles.label_styles["Tiny_Labels"])
                            Cal_Taken.place(x=100, y=150)
                            self.Taken_Cal.set(0)
                            Cal_remained = ctk.CTkLabel(Cal_Frame, text=f"Remaining Calories: \n{self.Remained_Cal}",
                                                    **Styles.label_styles["Tiny_Labels"])
                            Cal_remained.place(x=100, y=175)
                            self.Remained_Cal.set(Calories[0])
                            
                        elif Plan_Data["targetGoal"] == "Gain Weight":
                            ctk.CTkLabel(Cal_Frame, text=f"Target Calories:\n {Calories[0]}"
                                        , **Styles.label_styles["Tiny_Labels"]).place(x=100, y=125)
                            Cal_Taken = ctk.CTkLabel(Cal_Frame, text=f"Taken Calories: \n{self.Taken_Cal}",
                                                    **Styles.label_styles["Tiny_Labels"])
                            Cal_Taken.place(x=100, y=150)
                            self.Taken_Cal.set(0)
                            Cal_remained = ctk.CTkLabel(Cal_Frame, text=f"Remaining Calories: \n{self.Remained_Cal}",
                                                    **Styles.label_styles["Tiny_Labels"])
                            Cal_remained.place(x=100, y=175)
                            self.Remained_Cal.set(Calories[0])
                
                plus_image = ctk.CTkImage(dark_image=Image.open("Window_Images/plus.png"), size=(24, 24))
                for i, (Section, Details) in enumerate(self.Meals.items()):
                    F = ctk.CTkFrame(Cal_Frame, width=354, height=108, bg_color="grey")
                    F.grid(row=0 + i, column=2, pady=10)
                    F.grid_columnconfigure((0, 1, 2), weight=1)
                    F.grid_rowconfigure((0, 1, 2), weight=1)
                    ctk.CTkLabel(F, text=Section, **Styles.label_styles["Menu_Labels"]).grid(row=0, column=0, pady=5, padx=5)
                    ctk.CTkLabel(F, text=", ".join(Details["Name"]),  **Styles.label_styles["Menu_Labels"]).grid(row=1, column=0, pady=5, padx=5)
                    
                    ctk.CTkButton(F, text=" Add Meal",
                                image=plus_image, compound="left",
                                **Styles.label_styles["Menu_Labels"],
                                command= lambda: Open_mealSection(Section)
                                ).grid(row=2, column=2, pady=5, padx=(5, 10))
            if load_user_plan(Data_load["ID"]):
                Plan_starter()
            else:
                load_mainCalFrame()
        #============================================================================================================
        def Create_myPlan_Frame(section="My Plan"):
            switch_toSidebar(section)
            myPlan_Frame = ctk.CTkFrame(self.in_frame, border_color="white", border_width=2)
            self.switch_frame(myPlan_Frame)
            ctk.CTkLabel(myPlan_Frame, text="Welcome to part 3!!", **Styles.label_styles["Menu_Labels"]).place(x=469, y=276)
        def Create_Journey_Frame(section="Journey"):
            switch_toSidebar(section)
            Journey_Frame = ctk.CTkFrame(self.in_frame, border_color="white", border_width=2)
            self.switch_frame(Journey_Frame)
            ctk.CTkLabel(Journey_Frame, text="Welcome to part 3!!", **Styles.label_styles["Menu_Labels"]).place(x=469, y=276)
        def Create_Exercises_Frame(section="Exercises"):
            switch_toSidebar(section)
            Exe_Frame = ctk.CTkFrame(self.in_frame, border_color="white", border_width=2)
            self.switch_frame(Exe_Frame)
            ctk.CTkLabel(Exe_Frame, text="Welcome to part 3!!", **Styles.label_styles["Menu_Labels"]).place(x=469, y=276)
        def Open_Rate_us(section="Rate us!"):
            switch_toSidebar(section)
            Rate_Frame = ctk.CTkFrame(self.in_frame, border_color="white", border_width=2)
            self.switch_frame(Rate_Frame)
            ctk.CTkLabel(Rate_Frame, text="Welcome to part 3!!", **Styles.label_styles["Menu_Labels"]).place(x=469, y=276)
    def cleanup_exit(self):
        self.destroy()