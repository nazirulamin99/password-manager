import csv
import os
from datetime import datetime
from models import Password
from database import SessionLocal


def delete_password(pw_id):
    session = SessionLocal()
    password = session.query(Password).get(pw_id)
    if password:
        session.delete(password)
        session.commit()
    session.close()


def save_password_to_db(label, password):
    session = SessionLocal()
    new_pw = Password(label=label, password=password)
    session.add(new_pw)
    session.commit()
    session.close()


def get_all_passwords():
    session = SessionLocal()
    passwords = session.query(Password).order_by(Password.timestamp.desc()).all()
    session.close()
    return passwords


def export_passwords_to_csv(txt_file="passwords.txt", csv_file="passwords.csv"):
    if not os.path.exists(txt_file):
        return False # nothing to export
    
    with open(txt_file, "r") as txt, open(csv_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Label", "Password", "Timestamp"]) # csv headers

        for line in txt:
            parts = [p.strip() for p in line.strip().split("|")]
            if len(parts) == 3:
                writer.writerow(parts)
    return True


def save_password(label, password, filename="passwords.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, 'a') as f:
        f.write(f"{label} | {password} | {timestamp}\n")


def view_saved_passwords(filename="passwords.txt"):
    print("\n📂 Saved Passwords:\n" + "-"*30)
    try:
        with open (filename, 'r') as f:
            content = f.read()
            print(content if content else "No passwords saved yet.")
    except FileNotFoundError:
        print("No saved passwords found.")