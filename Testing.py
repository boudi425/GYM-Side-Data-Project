import customtkinter as ctk

print("CTk version:", ctk.__version__)

app = ctk.CTk()
app.geometry("600x400")

tabview = ctk.CTkTabview(app, width=400, height=300, tab_position="left")
tabview.place(x=100, y=50)

tabview.add("Tab 1")
tabview.add("Tab 2")

ctk.CTkLabel(tabview.tab("Tab 1"), text="You're in Tab 1").place(x=20, y=20)
ctk.CTkLabel(tabview.tab("Tab 2"), text="You're in Tab 2").place(x=20, y=20)

app.mainloop()
