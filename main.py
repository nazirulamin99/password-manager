from generator import generate_password
from utils import save_password, view_saved_passwords
import os
from time import sleep

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_bool_input(prompt):
    return input(prompt + "(y/n): ").strip().lower() == 'y'

def main():
    while True:
        print("🔐 Welcome to the Password Generator")

        # Get password length and validation
        while True:
            try: 
                length = int(input("Enter password length (e.g. 12): "))
                if length <= 0:
                    print("❌ Length must be greater than 0.")
                else:
                    break

            except ValueError:
                print("❌ Please enter a valid number.")

            # Get character type references
            use_upper = get_bool_input("Include uppercase letters?")
            use_digits = get_bool_input("Include numbers?")
            use_symbols = get_bool_input("Include symbols?")

            try:
                password = generate_password(length, use_upper, use_digits, use_symbols)
                print(f"\nGenerated Password: {password}")

            except Exception as e:
                print(f"❌ Error: {e}")            

            # Save option
            if get_bool_input("Do you want to save this password?"):
                label = input("Enter a label for this password (e.g. Gmail, Facebook): ")
                save_password(label, password)
                print("✅ Password saved to passwords.txt")

            # View saved passwords
            if get_bool_input("Do you want to view all saved passwords?"):
                view_saved_passwords()

            # Repeat or exit
            if not get_bool_input("\nDo you want to generate another password?"):
                print("\n👋 Goodbye!")
                sleep(1)
                break


if __name__ == "__main__":
    main()