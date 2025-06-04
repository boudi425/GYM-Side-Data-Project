import json

class user_session():
    def __init__(self, User_ID, Email, name):
        self.User_ID = User_ID
        self.Email = Email
        self.name = name
        


def save_session(session):
    with open("Session.json", "w") as f:
        json.dumps(session.__dict__, f)

def load_session():
    try:
        with open("session.json", "r") as f:
            data = json.loads(f)
            return user_session(**data)
    except FileNotFoundError:
        return None