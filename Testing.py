import customtkinter as ctk
from path_setup import add_frames_path
add_frames_path()
import Styles # type: ignore
import Side_Functions # type: ignore
from PIL import Image

Cal_Frame = ctk.CTk()
Cal_Frame.geometry("768x520")
Actual_Burn_cal = 2000
Main_Calories = [2300, 2500, 3000]
Diet_Goal = "Lose Weight"
Cal_Frame.grid_columnconfigure((0, 1, 2), weight=1)
def chosen_planDataLoad():
    pass

def load_mainCalFrame():
                def Open_mealSection(Section):
                    pass
                listOfMeals = ["Breakfast", "Lunch", "Dinner", "Snacks"]
                Taken_Cal = ctk.IntVar(value=0)
                Remained_Cal = ctk.IntVar(value=0)
                canvas_size = 250
                circle_padding = 30

                canvas = ctk.CTkCanvas(
                    Cal_Frame,
                    width=canvas_size,
                    height=canvas_size,
                    bg="#242424",
                    highlightthickness=0
                )
                canvas.grid(row=0, column=0, pady=5, sticky="w")

                canvas.create_oval(
                    circle_padding,
                    circle_padding,
                    canvas_size - circle_padding,
                    canvas_size - circle_padding,
                    fill="grey"
                )

                Calories = [2500, 2700, 3000]
                Plan_Data = {"Plan": "Plan1", "targetGoal": "Maintain My Weight"}
                for i in range(3):
                    if Plan_Data["Plan"] == f"Plan{i+1}":
                        if Plan_Data["targetGoal"] == "Maintain My Weight":
                            ctk.CTkLabel(Cal_Frame, text=f"Target Calories:\n {Calories[0]}", bg_color="grey"
                                        , **Styles.label_styles["Tiny_Labels"]).place(x=75, y=70)
                            Cal_Taken = ctk.CTkLabel(Cal_Frame, text=f"Taken Calories: \n{Taken_Cal}", bg_color="grey",
                                                    **Styles.label_styles["Tiny_Labels"])
                            Cal_Taken.place(x=75, y=110)
                            Cal_remained = ctk.CTkLabel(Cal_Frame, text=f"Remaining Calories: \n{Remained_Cal}", bg_color="grey"
                                                    ,**Styles.label_styles["Tiny_Labels"])
                            Cal_remained.place(x=73, y=155)
                            
                        elif Plan_Data["targetGoal"] == "Lose Weight":
                            ctk.CTkLabel(Cal_Frame, text=f"Target Calories:\n {Calories[0]}", bg_color="grey"
                                        , **Styles.label_styles["Tiny_Labels"]).place(x=75, y=70)
                            Cal_Taken = ctk.CTkLabel(Cal_Frame, text=f"Taken Calories: \n{Taken_Cal}",
                                                    **Styles.label_styles["Tiny_Labels"])
                            Cal_Taken.place(x=75, y=110)
                            Taken_Cal.set(0)
                            Cal_remained = ctk.CTkLabel(Cal_Frame, text=f"Remaining Calories: \n{Remained_Cal}",
                                                    bg_color="grey",
                                                    **Styles.label_styles["Tiny_Labels"])
                            Cal_remained.place(x=73, y=155)
                            Remained_Cal.set(Calories[0])
                            
                        elif Plan_Data["targetGoal"] == "Gain Weight":
                            ctk.CTkLabel(Cal_Frame, text=f"Target Calories:\n {Calories[0]}", bg_color="grey"
                                        , **Styles.label_styles["Tiny_Labels"]).place(x=75, y=70)
                            Cal_Taken = ctk.CTkLabel(Cal_Frame, text=f"Taken Calories: \n{Taken_Cal}",
                                                    **Styles.label_styles["Tiny_Labels"])
                            Cal_Taken.place(x=75, y=110)
                            Taken_Cal.set(0)
                            Cal_remained = ctk.CTkLabel(Cal_Frame, text=f"Remaining Calories: \n{Remained_Cal}",
                                                        bg_color="grey",
                                                    **Styles.label_styles["Tiny_Labels"])
                            Cal_remained.place(x=73, y=155)
                            Remained_Cal.set(Calories[0])
                plus_image = ctk.CTkImage(dark_image=Image.open("Window_Images/plus.png"), size=(24, 24))

                for i, Section in enumerate(listOfMeals):
                    print("Placing:", Section, "at row", i)
                    F = ctk.CTkFrame(Cal_Frame, width=354, height=108)
                    F.grid(row=i, column=2, pady=10, padx=5, sticky="n")

                    F.grid_columnconfigure(0, weight=1)

                    ctk.CTkLabel(F, text=Section, anchor="center", **Styles.label_styles["Menu_Labels"]
                                ).grid(row=0, column=0, pady=(10, 5))
                    ctk.CTkButton(F, text=" Add Meal", image=plus_image,
                                compound="left", **Styles.label_styles["Menu_Labels"],
                                command=lambda section=Section: Open_mealSection(section)
                                ).grid(row=1, column=0, pady=(5, 10))

load_mainCalFrame()
Cal_Frame.mainloop()