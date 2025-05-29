import customtkinter as ctk

class Dashboard_Window(ctk.CTk):
    def __init__(self, master):
        super().__init__(master)
        self.geometry("500x500")
        self.title("Nice")
        ctk.CTkLabel(self, text="NICE").pack(pady=10)
    