import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x200")

        # Create the slider
        self.slider = customtkinter.CTkSlider(
            self,
            from_=0,
            to=100,
            number_of_steps=100,
            command=self.update_slider_value
        )
        self.slider.pack(pady=20)

        # Create the label to display value
        self.slider_label = customtkinter.CTkLabel(self, text="Value: 0")
        self.slider_label.pack()

    def update_slider_value(self, value):
        self.slider_label.configure(text=f"Value: {int(float(value))}")

app = App()
app.mainloop()
