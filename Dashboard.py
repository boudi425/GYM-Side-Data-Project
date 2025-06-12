import customtkinter as ctk
import Styles
class mainMenu(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
    
    
    def Create_mainMenu_Frame(self):
        from Main import Main_Window
        Main_Window.geometry("1000x700")
        ctk.CTkLabel(self, text="Dashboard.", **Styles.label_styles["title2"]).pack()