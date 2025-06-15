import json

class user_session():
    def __init__(self, name, age, weight, height, Activity):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.Activity = Activity
        


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