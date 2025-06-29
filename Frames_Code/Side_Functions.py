import hashlib
import difflib
import os
import secrets
import sqlite3
from PIL import Image, ImageDraw
import random
import requests

def mask_email(email):
    name, domain = email.split("@")
    if len(name) < 3:
        return email  # too short to mask
    return f"{name[0]}{'*' * (len(name)-2)}{name[-1]}@{domain}"

def generate_random_num(Range_Num):
    Numbers = []
    for i in range(Range_Num):
        Numbers.append(str(random.randint(0, 10)))
    return "".join(Numbers)
def generate_token():
    return secrets.token_hex(32)  # Generates a 64-char secure token

def suggest_email_domain(email):
    if "@" in email:
        name, domain = email.split("@")
        valid = ["gmail.com", "hotmail.com", "yahoo.com"]
        if domain not in valid:
            suggestion = difflib.get_close_matches(domain, valid, n=2, cutoff=0.8)
            if suggestion:
                return f"Did you mean {name}@{suggestion[0]}?"
    return None

def check_empty(entry, warning_label, message):
        if isinstance(entry.get(), str):
            if entry.get().strip() == "" or entry.get() == "0":
                warning_label.configure(text=message)
                return False
            else:
                warning_label.configure(text="")
                return True
        if isinstance(entry.get(), int):
            if entry.get() == 0:
                warning_label.configure(text=message)
                return False
            else:
                warning_label.configure(text="")
                return True

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()  # Hash the password

def verify_password(input_password, stored_hash):
    return hash_password(input_password) == stored_hash  # Compare hashes

def cleanup_exit():
    if os.path.exists("User_Out_Data/Session.json"):
        os.remove("User_Out_Data/Session.json")
        
def openData(DataName, File_Query=None):
    Con = sqlite3.connect(DataName)
    Cur = Con.cursor()
    if File_Query:
        with open(File_Query, "r") as query:
            Cur.executescript(query.read())
    return Con, Cur

def make_circle_image(path, size=(100, 100)):
    img = Image.open(path).resize(size).convert("RGBA")

    # Create same size mask image with transparency
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size[0], size[1]), fill=255)

    # Apply the mask to create circular image
    img.putalpha(mask)
    return img

def Get_Malnutrition(Food_Query, grams=100):
    with open("User_Out_Data/Api_Key.txt") as api_key:
        api_key = api_key.read()
    search = requests.get(f"https://api.nal.usda.gov/fdc/v1/foods/search?query={Food_Query}&api_key={api_key}").json()
    fdc_id = search["foods"][0]["fdcId"]
    
    food = requests.get(f"https://api.nal.usda.gov/fdc/v1/food/{fdc_id}?api_key={api_key})").json()
    
    nutrients = {n["nutrientName"]: n["value"] for n in food["foodNutrients"]}
    Cal = round((nutrients.get("Energy (Atwater General Factors)", 0) / 100) * grams, 2)
    protein = round((nutrients.get('Protein', 0) / 100) * grams, 2)
    carbs = round((nutrients.get('Carbohydrate, by difference', 0) / 100) * grams, 2)
    fats = round((nutrients.get('Total lipid (fat)', 0) / 100) * grams, 2)
    
    return {
        "food": Food_Query,
        "grams": grams,
        "Calories": Cal,
        "Protein": protein,
        "Carbs": carbs,
        "Fats": fats
    }

def search_foods(query, limit=5):
    with open("User_Out_Data/Api_Key.txt") as api_key:
        api_key = api_key.read()
    response = requests.get(f"https://api.nal.usda.gov/fdc/v1/foods/search?query={query}&pageSize={limit}&api_key={api_key}")
    foods = response.get('foods', [])
    if not foods:
        return []
    
    results = []
    for food in foods:
        results.append({
            f"{food["description"]}": food["fdcId"]
        })
    return results

def only_digits(char):
    return char.isdigit()