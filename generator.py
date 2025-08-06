import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    characters = list(string.ascii_lowercase)

    if use_upper:
        characters += list(string.ascii_uppercase)
    if use_digits:
        characters += list(string.digits)
    if use_symbols:
        characters += list("!@#$%^&*()-_=+[]{}|;:,.<>?")

    if not characters:
        raise ValueError("No character types selected!")
    
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


