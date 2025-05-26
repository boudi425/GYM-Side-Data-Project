import difflib

def suggest_email_domain(email):
    if "@" in email:
        name, domain = email.split("@")
        valid = ["gmail.com", "hotmail.com", "yahoo.com"]
        suggestion = difflib.get_close_matches(domain, valid, n=1, cutoff=0.8)
        if suggestion:
            return f"Did you mean {name}@{suggestion[0]}?"
    return None

