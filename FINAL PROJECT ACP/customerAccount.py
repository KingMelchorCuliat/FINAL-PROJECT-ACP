import json # This library is used for saving data like customer accounts and customer feedbacks
from argon2 import PasswordHasher # This library is used for securing the customer password
import re # This library is used for giving a requirements for the passwords

# Class that managing customer accounts
class customerAccount:
    def __init__(self, account_file='customerAccounts.json'):
        self.account_file = account_file
        self.ph = PasswordHasher()
        
    def requiredStrongPassword(self, password):
        if not re.search(r'\d', password) or not re.search(r'[A-Z]', password):
            return "Password must contain at least one number and one capital letter."
        return None

    def load_accounts(self):
        try:
            with open(self.account_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Account file not found, initializing a new file.")
            return {}

    def save_accounts(self, accounts):
        try:
            with open(self.account_file, 'w') as file:
                json.dump(accounts, file, indent=4)
        except IOError as e:
            print(f"Error saving accounts: {e}")

    def create_account(self):
        accounts = self.load_accounts()
        user_id = len(accounts) + 1

        while True:
            username = input("Enter the username you want (must be 6 characters long): ")
            if len(username) < 6:
                print("Username must be at least 6 characters long.")
            elif username in accounts:
                print("Sorry, that username is already taken. Please choose a different username.")
            else:
                break

        while True:
            password = input("Enter a strong password (must have at least one capital letter and one number): ")
            password_check = self.requiredStrongPassword(password)
            if password_check:
                print(password_check)
            else:
                break

        hashed_password = self.ph.hash(password)
        accounts[username] = {'user_id': user_id, 'password': hashed_password}
        self.save_accounts(accounts)

        print("----------------------------------------------------------")
        print(f"Welcome {username}, your account was created successfully!")
        return user_id

    def login(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        accounts = self.load_accounts()

        if username in accounts:
            stored_hash = accounts[username]['password']
            try:
                self.ph.verify(stored_hash, password)
                print("---------------------------------------")
                print(f"Login successful! Welcome, {username}.")
                return accounts[username]['user_id']
            except Exception:
                print("Invalid password.")
        else:
            print("Invalid username or password.")
        return None
