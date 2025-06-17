import hashlib
import difflib
import os
import secrets
import sqlite3

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