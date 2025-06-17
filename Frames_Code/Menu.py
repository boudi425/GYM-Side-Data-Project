import customtkinter as ctk
import Styles
from User_session import load_session
from PIL import Image

class mainMenu(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.Create_mainMenu_Frame()

    def Create_mainMenu_Frame(self):
        Data_Load = load_session()

        # ---------------------- Title Label ----------------------
        ctk.CTkLabel(self, text="BLACK GYM Main Menu", **Styles.label_styles["Menu_title"]).place(x=24, y=11)

        # ---------------------- Load Images ----------------------
        image_paths = {
            "logout": "Window_Images/logout.png",
            "profile": "Window_Images/Profile.png",
            "settings": "Window_Images/Sett.png",
            "calorie": "Window_Images/Cal.png",
            "exercise": "Window_Images/Exe.png",
            "goal": "Window_Images/Progress.png",
            "plan": "Window_Images/Plan.png",
            "feedback": "Window_Images/Feedback.png",
        }

        images = {key: ctk.CTkImage(dark_image=Image.open(path), size=(30, 30)) for key, path in image_paths.items()}
        small_images = {key: ctk.CTkImage(dark_image=Image.open(path), size=(24, 24)) for key, path in image_paths.items()}

        # ---------------------- Main Display Frame ----------------------
        self.In_frame = ctk.CTkFrame(self, width=768, height=520, fg_color="gray20", border_width=2, border_color="white")
        self.In_frame.place(x=220, y=70)

        # ---------------------- Top Buttons ----------------------
        top_buttons = [
            {"text": "Profile", "image": small_images["profile"], "style": "First", "x": 500},
            {"text": "Settings", "image": small_images["settings"], "style": "Second", "x": 672},
            {"text": "Logout", "image": small_images["logout"], "style": "Logout", "x": 840},
        ]

        for btn in top_buttons:
            b = ctk.CTkButton(self, text=f" {btn['text']}", image=btn["image"],
                              **Styles.button_styles[btn["style"]],
                            width=150, height=50, compound="left")
            b.place(x=btn["x"], y=11)
            b.bind("<Enter>", lambda e, b=b: b.configure(cursor="hand2"))

        # ---------------------- Sidebar Buttons ----------------------
        side_buttons = [
            {"text": "My Plan", "image": images["plan"], "style": "Sidebar", "y": 110},
            {"text": "Calories", "image": images["calorie"], "style": "First", "y": 190},
            {"text": "Exercises", "image": images["exercise"], "style": "Sidebar", "y": 270},
            {"text": "Journey", "image": images["goal"], "style": "Sidebar", "y": 350},
            {"text": "Rate us!", "image": images["feedback"], "style": "Feedback", "y": 528},
        ]

        for btn in side_buttons:
            b = ctk.CTkButton(self, text=btn["text"], image=btn["image"],
                              **Styles.button_styles[btn["style"]],
                            width=184, height=50, compound="left")
            b.place(x=24, y=btn["y"])
            b.bind("<Enter>", lambda e, b=b: b.configure(cursor="hand2"))
