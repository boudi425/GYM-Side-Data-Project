from path_setup import add_frames_path, get_data_path
add_frames_path()
import customtkinter as ctk
from mainMenu import Dashboard # type: ignore

def show_dashboard():
    first_page.destroy()
    start = Dashboard()  # This will create the new window
    start.run()  # This will start the main loop of the Dashboard
first_page = ctk.CTk()
first_page.title("Welcome")

login_btn = ctk.CTkButton(first_page, text="Login", command=show_dashboard)
login_btn.pack()

first_page.mainloop()