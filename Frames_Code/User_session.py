import json
import os 
class user_session:
    def __init__(self, ID, name, age, weight, height, Activity, Image=None):
        self.ID = ID
        self.name = name
        self.Activity = Activity
        self.weight = weight
        self.height = height
        self.age = age
        self.Image = Image

def save_session(session):
    with open("User_Out_Data/Session.json", "w") as f:
        json.dump(session.__dict__, f)

def load_session():
    try:
        with open("User_Out_Data/Session.json", "r") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        return None
class UserSettings:
    def __init__(self, theme, colors, font_size, font_type, Notifications, Data):
        self.theme = theme
        self.colors = colors
        self.font_size = font_size
        self.font_type = font_type
        self.Notifications = Notifications
        self.Data = Data
        
def save_settings(ID, Settings):
    os.makedirs("User_Out_Data", exist_ok=True)
    with open(f"User_Out_Data/User{ID}_Settings.json", "w") as f:
        json.dump(Settings.__dict__, f, indent=4)

def load_user_Settings(ID):
    try:
        with open(f"User_Out_Data/User{ID}_Settings.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        # Default settings
        return {
            "theme": "dark",
            "colors": "blue",
            "font_size": 16,
            "font_type": "Lato",
            "Notifications": False,
            "Data": False
        }
        
class UserPlan:
    def __init__(self, Plan, targetGoal):
        self.Plan = Plan
        self.targetGoal = targetGoal

        
def save_Plan(ID, userSelection):
    os.makedirs("User_Out_Data", exist_ok=True)
    with open(f"User_Out_Data/User{ID}_Plan.json", "w") as f:
        json.dump(userSelection.__dict__, f, indent=4)

def load_user_plan(ID):
    try:
        with open(f"User_Out_Data/User{ID}_Plan.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        # Default settings
        return None
    
class UserMealData:
    def __init__(self, Date, mealType, foodNames, grams, Kcal):
        self.Date = Date
        self.mealType = mealType
        self.foodNames = foodNames
        self.grams =  grams
        self.Kcal = Kcal
    
def saveMealData(ID, mealType, Data):
    os.makedirs("User_Out_Data", exist_ok=True)
    with open(f"User_Out_Data/User{ID}_{mealType}.json", "w") as f:
        json.dump(ID.__dict__, f, indent=4)
        
def loadMealData(ID, mealType):
    try:
        with open(f"User_Out_Data/User{ID}_{mealType}.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    
def deleteMealData(ID, mealType):
    file_path = f"User_Out_Data/User{ID}_{mealType}.json"
    try:
        os.remove(file_path)
        return True
    except FileNotFoundError:
        return False