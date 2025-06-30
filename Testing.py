import customtkinter as ctk
from path_setup import add_frames_path
add_frames_path()
import Styles # type: ignore
import Side_Functions # type: ignore
from PIL import Image
import  datetime
Cal_Frame = ctk.CTk()
Cal_Frame.geometry("768x520")
Actual_Burn_cal = 2000
Main_Calories = [2300, 2500, 3000]
Diet_Goal = "Maintain My Weight"
Cal_Frame.grid_columnconfigure((0, 1, 2), weight=1)

Cal_Frame.mainloop()