import datetime # library used to display the date and time when the feedback is submitted
import json # library used to store the datas like customer accounts and customer feedback
from argon2 import PasswordHasher # library used to secure the customer password
import re # library used for requiring a strong password

# Class that managing customer accounts
class customerAccount:
    def __init__(self, account_file='customerAccounts.json'):
        self.account_file = account_file
        self.ph = PasswordHasher()
        
    def  requiredStrongPassword(self, password):
        if not re.search(r'\d', password) or not re.search(r'[A-Z]', password):
            return "Password must contain at least one number and one capital letter."
        return None

    def load_accounts(self): # for loading the accounts in json file
        try:
            with open(self.account_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Account file not found, initializing a new file.")
            return {}
        
    def save_accounts(self, accounts): # for saving accounts in json file
        try:
            with open(self.account_file, 'w') as file:
                json.dump(accounts, file, indent=4)
        except IOError as e:
            print(f"Error saving accounts: {e}")

    def create_account(self):
        accounts = self.load_accounts()
        user_id = len(accounts) + 1 

        while True:
            username = input("Enter the username you want: ")
            if len(username) < 6:
                print("Username must be at least 6 characters long.") # requirements for usernames
            elif username in accounts:
                print("Username already taken. Please choose a different username.")
            else:
                break  

        while True:
            password = input("Enter a strong password (must have at least one capital letter and one number): ")

            password_check = self.requiredStrongPassword(password)
            if password_check:
               print(password_check) 
            else:
               break  

        #hashed password using argon2
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
    

#Class that managing customer Feedbacks
class Feedback:
    def __init__(self, user_id, name, feedback, rating):
        self.feedback_id = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f") 
        self.user_id = user_id
        self.name = name
        self.feedback = feedback
        self.rating = rating
        self.timestamp = datetime.datetime.now()
        self.suggestion = None

    def customer_suggestion(self):
        if self.rating <= 2:  
            print("\nIt seems that you are not satisfied with our product.")
            user_suggestion = input("Would you like to provide a suggestion for improvements? (yes/no): ")
            if user_suggestion.lower() == 'yes':
                self.suggestion = input("Please provide your suggestion: ")
                print("Thank you for your suggestion!")


def load_customerFeedback(filename='customerFeedback.json'): # for loading feedbacks in json file
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Feedback file not found. Creating a new one.")
        return {}

def save_customerFeedback(products, filename='customerFeedback.json'): # for saving feedback in json file
    data = {}
    for product_id, product_data in products.items():
        data[product_id] = {
            'productName': product_data['productName'],
            'productCategory': product_data['productCategory'],
            'feedbacks': [{'feedback_id': feedback.feedback_id,
                           'user_id': feedback.user_id,
                           'name': feedback.name,
                           'feedback': feedback.feedback,
                           'rating': feedback.rating,
                           'suggestion': feedback.suggestion,
                           'timestamp': feedback.timestamp.strftime('%Y-%m-%d %H:%M:%S')} 
                          for feedback in product_data['feedbacks']]
        }
    
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        print(f"Error saving feedback data: {e}")
        

def get_customerFeedback(user_id):
    name = input("\nEnter your name or type Anonymous: ")
    feedback = input("Enter your feedback: ")
    while True:
        try:
            rating = int(input("On a scale of 1 to 5 (1 = very dissatisfied, 5 = very satisfied), give your rating: "))
            if 1 <= rating <= 5:
                break
            else:
                print("Invalid input. Please enter a number between 1 and 5.")
        except ValueError:
            print("You can only enter a number.")

    return Feedback(user_id, name, feedback, rating)

def view_customerFeedbacks(products):
    print("\nList of all products with feedback:")
    any_feedback = False
    for product_id, product_data in products.items():
        feedbacks = product_data.get('feedbacks', [])
        if feedbacks:
            any_feedback = True
            print(f"\nFeedback for {product_data['productName']} (ID: {product_id}):")
            for feedback in feedbacks:
                print(f"Feedback ID: {feedback.feedback_id}")
                print(f"User ID: {feedback.user_id}")
                print(f"User: {feedback.name}")
                print(f"Rating: {feedback.rating}")
                print(f"Feedback: {feedback.feedback}")
                print(f"Suggestion: {feedback.suggestion or 'No suggestion provided'}")
                print(f"Date: {feedback.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
                print("-" * 50)
            avg_rating = sum(f.rating for f in feedbacks) / len(feedbacks)
            print(f"Average Rating: {avg_rating:.1f}/5.0")
            print("=" * 60)
    if not any_feedback:
        print("No feedback has been given for any product.")
        
# for adding products that not on the list
def addProduct(products):
    print("\nAdd New Product:")
    print("--------------------")
    product_name = input("Enter the product name: ")
    product_category = input("Enter the product category: ")

    new_product_id = max(products.keys()) + 1 if products else 1 # assigning new id for new products
    products[new_product_id] = {
        'productName': product_name,
        'productCategory': product_category,
        'feedbacks': []
    }

    print(f"New product '{product_name}' added successfully!")


def select_fromProducts(products):
    print("\nThis products are our best sellers, select any to give your feedback.")
    print("Select the product you want to give feedback on:")
    for product_id, product_data in products.items():
        print(f"{product_id}. {product_data['productName']} - {product_data['productCategory']}")

    while True:
        try:
            selected_id = int(input("Enter the product ID: "))
            if selected_id in products:
                return products[selected_id]
            else:
                print("Invalid product ID. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter only an integer.")
            
def main():
    products = {
        1: {'productName': "Rocking Chair", 'productCategory': "Furniture", 'feedbacks': []},
        2: {'productName': "Dining Table", 'productCategory': "Furniture", 'feedbacks': []},
        3: {'productName': "chaise Lounge Couch", 'productCategory': "Furniture", 'feedbacks': []},
        4: {'productName': "Corner Book Case", 'productCategory': "Furniture", 'feedbacks': []},
        5: {'productName': "Media Chest Drawer", 'productCategory': "Furniture", 'feedbacks': []},
    }

    customer_account = customerAccount()

    while True:
        print("Welcome to Share your Experience: Product Feedback System")
        print("----------------------------------------------------------")
        print("1. Create Account")
        print("2. Log in")
        choice = input("Enter your choice: ")

        if choice == '1':
            user_id = customer_account.create_account()
            if user_id:
                break
        elif choice == '2':
            user_id = customer_account.login()
            if user_id:
                break
        else:
            print("Invalid input. Please try again.")

    while True:
        print("\nProduct Feedback System Menu:")
        print("------------------------------------------")
        print("1. Provide Feedback to a Product")
        print("2. View Feedbacks")
        print("3. Add a product that are not on the list")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            product = select_fromProducts(products)
            feedback = get_customerFeedback(user_id)
            if feedback:
                feedback.customer_suggestion()
                product['feedbacks'].append(feedback)
                save_customerFeedback(products)
        elif choice == '2':
            view_customerFeedbacks(products)
        elif choice == '3':
            addProduct(products)
        elif choice == '4':
            print("Exiting the program. Thank you for your cooperation, we will improve our products more!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
