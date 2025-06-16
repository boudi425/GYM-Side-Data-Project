import customtkinter as ctk
import Styles
from User_session import load_session, save_session, user_session
import Side_Functions
import os
import sys
import sqlite3
import webbrowser
class mainMenu(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.Create_mainMenu_Frame()
    def Create_mainMenu_Frame(self):
        Data_Load = load_session()
        ctk.CTkLabel(self, text="BLACK GYM Main Menu", **Styles.label_styles["title2"]).place(x=24, y=11)