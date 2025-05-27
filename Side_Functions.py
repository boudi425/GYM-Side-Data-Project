import hashlib
import difflib

def suggest_email_domain(email):
    if "@" in email:
        name, domain = email.split("@")
        valid = ["gmail.com", "hotmail.com", "yahoo.com"]
        suggestion = difflib.get_close_matches(domain, valid, n=1, cutoff=0.8)
        if suggestion:
            return f"Did you mean {name}@{suggestion[0]}?"
    return None

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()  # Hash the password

def verify_password(input_password, stored_hash):
    return hash_password(input_password) == stored_hash  # Compare hashes
