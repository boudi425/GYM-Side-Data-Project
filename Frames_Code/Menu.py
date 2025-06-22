import customtkinter as ctk
import Styles
from User_session import load_session
from PIL import Image

class mainMenu(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.allTab_buttons = {}
        self.allSidebar_buttons = {}
        self.Create_mainMenu_Frame()

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
            
        def Open_Settings(section="Settings"):
            switch_toTab(section)
            Sett_Top = ctk.CTkToplevel()

        def Open_Profile(section="Profile"):
            switch_toTab(section)
            Profile_Top = ctk.CTkToplevel()
            
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
        def Create_Calories_Frame(section="Calories"):
            switch_toSidebar(section)
            Cal_Frame = ctk.CTkFrame(self.in_frame, border_color="white", border_width=2)
            self.switch_frame(Cal_Frame)
            ctk.CTkLabel(Cal_Frame, text="Welcome to part 3!", **Styles.label_styles["Menu_Labels"]).place(x=469, y=276)
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
        
