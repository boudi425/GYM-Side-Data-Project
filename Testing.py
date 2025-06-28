import customtkinter as ctk
from path_setup import add_frames_path
add_frames_path()
import Styles # type: ignore
import Side_Functions # type: ignore
Cal_Frame = ctk.CTk()
Cal_Frame.geometry("768x520")
Actual_Burn_cal = 2000
Main_Calories = [2300, 2500, 2700]
Diet_Goal = "Gain Weight"
Cal_Frame.grid_columnconfigure((0, 1, 2), weight=1)
Cal_Frame.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
def chosen_planDataLoad():
    pass

for i, Calories_Plan in enumerate(Main_Calories):
                    Plan_Frame = ctk.CTkFrame(Cal_Frame,
                                        width=150, height=400,
                                        border_color="#9FA8DA", border_width=2)
                    Plan_Frame.grid(row=1, column=i, pady=15, padx=10)
                    ctk.CTkLabel(Plan_Frame, text=f"Plan{i+1}",
                                **Styles.label_styles["Menu_Labels_Tiny"]).grid(row=0, column=0, pady=10)
                    ctk.CTkLabel(Plan_Frame, text=f"Target Calories: {Calories_Plan}").grid(row=1, column=0, pady=5)
                    
                    if Diet_Goal == "Maintain My Weight":
                        ctk.CTkLabel(Plan_Frame, text="Target Burned Calories: 220",
                                    **Styles.label_styles["Menu_Labels_Tiny"]).grid(row=2, column=0, pady=5, padx=10)
                        ctk.CTkLabel(Plan_Frame, text="Note: Just Eat Healthy \nand stick to your Target Calories",
                                    **Styles.label_styles["Menu_Labels_Tiny"]).grid(row=3, column=0, pady=5, padx=10)
                        ctk.CTkButton(Plan_Frame,
                                    text="Choose",
                                    width=110, height=35,
                                    **Styles.button_styles["Quick"],
                                    command= lambda: chosen_planDataLoad("Plan", "Maintain My Weight")).grid(row=4, column=0, padx=10)
                        
                    elif Diet_Goal == "Lose Weight":
                        Target_burn =  Calories_Plan - Actual_Burn_cal
                        ctk.CTkLabel(Plan_Frame, text=f"Target Burned Calories: {Target_burn - 15}",
                                    **Styles.label_styles["Menu_Labels_Tiny"]).grid(row=2, column=0, pady=5)
                        if Target_burn <= 300:
                            noteText = "Burn From Running,\n Exercises Even Walking!,\n Just Make sure to Relax!"
                            ctk.CTkLabel(Plan_Frame, text=f"Note: {noteText}",
                                        **Styles.label_styles["Menu_Labels_Tiny"]).grid(row=3, column=0, pady=5, padx=5)
                            ctk.CTkLabel(Plan_Frame, text="0.25 kg loss per week",
                                        **Styles.label_styles["Menu_Labels_Tiny"]).grid(row=4, column=0, pady=15)
                            ctk.CTkButton(Plan_Frame,
                                    text="Choose",
                                    width=110, height=35,
                                    **Styles.button_styles["Quick"],
                                    command= lambda: chosen_planDataLoad("Plan1", "Lose Weight")).grid(row=5, column=0, pady=15)
                            
                        elif Target_burn > 300 and Target_burn <= 750:
                            noteText = "Going to be tough\n but with something like hit cardio will do fine!"
                            ctk.CTkLabel(Plan_Frame, text=f"Note: {noteText}",
                                        **Styles.label_styles["Menu_Labels_Tiny"]).grid(row=2, column=0, pady=5, padx=5)
                            ctk.CTkLabel(Plan_Frame, text="0.30 - 0.5 kg loss per week",
                                        **Styles.label_styles["Menu_Labels_Tiny"]).grid(row=4, column=0, pady=5)
                            ctk.CTkButton(Plan_Frame,
                                    text="Choose",
                                    width=110, height=35,
                                    **Styles.button_styles["Quick"],
                                    command= lambda: chosen_planDataLoad("Plan2", "Lose Weight")).grid(row=5, column=0, pady=15)
                            
                        elif Target_burn >= 750:
                            noteText = "This is Extreme Weight Loss, Know that doing this for more than two weeks may affect health!"
                            ctk.CTkLabel(Plan_Frame, text=f"Note: {noteText}",
                                        **Styles.label_styles["Menu_Labels_Tiny"]).grid(row=3, column=0, pady=5)
                            ctk.CTkLabel(Plan_Frame, text="0.75kg -- 1kg loss per week",
                                        **Styles.label_styles["Menu_Labels_Tiny"]).grid(row=4, column=0, pady=5, padx=10)
                            ctk.CTkButton(Plan_Frame,
                                    text="Choose",
                                    width=110, height=35,
                                    **Styles.button_styles["Quick"],
                                    command= lambda: chosen_planDataLoad("Plan3", "Lose Weight")).grid(row=5, column=0, pady=15)
                            
                    elif Diet_Goal == "Gain Weight":
                        Calories_Diff = Calories_Plan - Actual_Burn_cal
                        ctk.CTkLabel(Plan_Frame, text=f"Cardio if wanted: 15 - 30 min cardio",
                                    **Styles.label_styles["Menu_Labels_Tiny"]).grid(row=2, column=0, pady=5)
                        if Calories_Diff <= 300:
                            noteText = "Make sure your diet is full of Carbs and Proteins!"
                            ctk.CTkLabel(Plan_Frame, text=f"Note: {noteText}",
                                        **Styles.label_styles["Menu_Labels_Tiny"]).grid(row=3, column=0, pady=5)
                            ctk.CTkLabel(Plan_Frame, text="0.25 kg gain per week",
                                        **Styles.label_styles["Menu_Labels_Tiny"]).grid(row=4, column=0, pady=5)
                            ctk.CTkButton(Plan_Frame,
                                    text="Choose",
                                    width=110, height=35,
                                    **Styles.button_styles["Quick"],
                                    command= lambda: chosen_planDataLoad("Plan1", "Gain Weight")).grid(row=5, column=0, pady=15)
                            
                        elif Calories_Plan > 300 and Calories_Diff >= 750:
                            noteText = "Make sure you are clean in terms of food sources and don't overdo yourself!"
                            ctk.CTkLabel(Plan_Frame, text=f"Note: {noteText}",
                                        **Styles.label_styles["Menu_Labels_Tiny"]).grid(row=3, column=0, pady=5, padx=10)
                            ctk.CTkLabel(Plan_Frame, text="0.30 - 0.5 kg gain per week",
                                        **Styles.label_styles["Menu_Labels_Tiny"]).grid(row=4, column=0, pady=5, padx=10)
                            ctk.CTkButton(Plan_Frame,
                                    text="Choose",
                                    width=110, height=35,
                                    **Styles.button_styles["Quick"],
                                    command= lambda: chosen_planDataLoad("Plan2", "Gain Weight")).grid(row=5, column=1, pady=15)
                            
                        elif Calories_Diff >= 750:
                            noteText = "This will gain but will gain fats as much as muscles so make sure to checkout our lost plans after!"
                            ctk.CTkLabel(Plan_Frame, text=f"Note: {noteText}",
                                        **Styles.label_styles["Menu_Labels_Tiny"]).grid(row=3, column=0, pady=5, padx=10)
                            ctk.CTkLabel(Plan_Frame, text="0.75kg -- 1kg gain per week",
                                        **Styles.label_styles["Menu_Labels_Tiny"]).grid(row=4, column=0, pady=5, padx=10)
                            ctk.CTkButton(Plan_Frame,
                                    text="Choose",
                                    width=110, height=35,
                                    **Styles.button_styles["Quick"],
                                    command= lambda: chosen_planDataLoad("Plan3", "Gain Weight")
                                    ).grid(row=5, column=1, pady=15)
Cal_Frame.mainloop()