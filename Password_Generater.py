# Import necessary libraries
import hashlib
import secrets 
import string
import datetime
import time

# Define a class for the PasswordGenerator
class PasswordGenerator:
    def __init__(self):
        # Get user's name for personalized greetings
        self.user_name = input("👋 Hello there! What's your name? ")
        # Generate a greeting message based on current time, date, and day
        self.greeting = self.get_greeting()
        # Initialize an empty list to store saved passwords
        self.passwords = []

    # Generate a personalized greeting message
    def get_greeting(self):
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        current_day = datetime.datetime.now().strftime("%A")
        return f"🌞 Good day, {self.user_name}! It's {current_time} on {current_date}, {current_day}."

    # Function to generate a password using provided characters and length
    def generate_password(self, length, characters):
        return ''.join(secrets.choice(characters) for _ in range(length))

    # Generate a numeric password
    def generate_numeric_password(self, length):
        return self.generate_password(length, string.digits)

    # Generate an alphanumeric password
    def generate_alphanumeric_password(self, length):
        return self.generate_password(length, string.ascii_letters + string.digits)

    # Generate a password with special characters
    def generate_special_password(self, length):
        return self.generate_password(length, string.ascii_letters + string.digits + string.punctuation)

    # Generate a custom password using a name and random numeric
    def generate_custom_password(self, name, length):
        max_name_length = length - 4
        truncated_name = name[:max_name_length]
        random_numeric = self.generate_numeric_password(length - len(truncated_name))
        return f"{truncated_name}{random_numeric}"

    # Hash a given password using SHA-256 algorithm
    def hash_password(self, password):
        sha256_hash = hashlib.sha256(password.encode()).hexdigest()
        return sha256_hash

    # Save a password to the list of saved passwords
    def save_to_file(self, password, website_name):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.passwords.append({
            "timestamp": timestamp,
            "website_name": website_name,
            "password": password
        })

    # Display the list of saved passwords with details
    def display_saved_passwords(self):
        print("\n🔐 Saved Passwords:")
        for password in self.passwords:
            print("📅 Timestamp:", password["timestamp"])
            print("🌐 Website/Application:", password["website_name"])
            print("🔑 Password:", password["password"])
            print("-" * 40)

    # Evaluate the strength of a password and return a complexity level
    def evaluate_password_strength(self, password):
        complexity = "Weak"
        if any(c.isdigit() for c in password) and any(c.isalpha() for c in password) and any(c in string.punctuation for c in password):
            complexity = "Strong"
        elif any(c.isdigit() for c in password) and any(c.isalpha() for c in password):
            complexity = "Medium"
        return complexity

    # Copy text to clipboard (requires pyperclip module)
    def copy_to_clipboard(self, text):
        try:
            import pyperclip
            pyperclip.copy(text)
            print("📋 Password copied to clipboard!")
        except ImportError:
            print("❌ Clipboard integration is not supported on your system.")

    # Main function to run the password generator program
    def main(self):
        print(self.greeting)
        print("🚀 Welcome to the Most Advanced Password Generator Program")
        print("🔐 Created by Anubhav Chaurasia\n")

        while True:
            # Get the name of the website or application
            website_name = input("\n🌐 Enter the name of the website or application for which you want to create a super-secure password: ")
            print("\n🚀 Generating a password for:", website_name)

            print("\n🛠 Choose the password type:")
            print("1. Numeric Only")
            print("2. Alphanumeric")
            print("3. Alphanumeric + Special Characters")
            print("4. Custom Password (Desired Name + Numeric)")
            print("5. Display Saved Passwords")
            print("6. Exit")

            try:
                option = int(input("🔢 Enter your choice: "))

                if option == 6:
                    print("🚀 Exiting program...")
                    time.sleep(2)
                    print("")
                    print("🌟 Have an amazing day ahead!")
                    time.sleep(10)
                    break
                elif option < 1 or option > 6:
                    print("❌ Invalid option. Please enter a valid choice.")
                    continue

                if option != 5:
                    password_length = int(input("🔑 Enter the desired password length: "))

                if option == 1:
                    password = self.generate_numeric_password(password_length)
                elif option == 2:
                    password = self.generate_alphanumeric_password(password_length)
                elif option == 3:
                    password = self.generate_special_password(password_length)
                elif option == 4:
                    desired_name = input("📛 Enter a desired name/word: ")
                    if len(desired_name) >= password_length - 4:
                        print("❌ Desired name/word is too long for this password length.")
                        continue
                    password = self.generate_custom_password(desired_name, password_length)

                print("\n🔐 Password generated for:", website_name)
                print("🔒 Generated Password:", password)
                strength = self.evaluate_password_strength(password)
                print("🌟 Password Strength:", strength)

                if strength == "Weak":
                    print("🔴 This password is weak. Make it stronger!")
                elif strength == "Medium":
                    print("🟡 This password is of intermediate strength.")
                else:
                    print("🟢 This password is strong and secure!")

                hashed_password = self.hash_password(password)
                print("🔑 Hashed Password:", hashed_password)

                save_choice = input("💾 Do you want to save this password? (yes/no): ").lower()
                if save_choice == "yes":
                    self.save_to_file(password, website_name)
                    print("📝 Password saved.")

                clipboard_choice = input("📋 Do you want to copy the password to clipboard? (yes/no): ").lower()
                if clipboard_choice == "yes":
                    self.copy_to_clipboard(password)

            except ValueError:
                print("❌ Invalid input. Please enter a valid option or value.")

# Run the program if executed as a standalone script
if __name__ == "__main__":
    generator = PasswordGenerator()
    generator.main()