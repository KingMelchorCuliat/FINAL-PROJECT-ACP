from customerAccount import customerAccount
from Feedback import Feedback, load_customerFeedback, save_customerFeedback

def get_customerFeedback(user_id):
    name = input("\nEnter your name or type Anonymous: ")
    feedback = input("Enter a feedback: ")
    while True:
        try:
            rating = int(input("On a scale of 1 to 5 (1 = very dissatisfied, 5 = very satisfied), give your rating: "))
            if 1 <= rating <= 5:
                break
            else:
                print("Invalid input. Please enter a number between 1 and 5.")
        except ValueError:
            print("Sorry, but you can only enter a number.")
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

def addProduct(products):
    print("\nAdd New Product:")
    product_name = input("Enter the product name: ")
    product_category = input("Enter the product category: ")

    new_product_id = max(products.keys()) + 1 if products else 1
    products[new_product_id] = {
        'productName': product_name,
        'productCategory': product_category,
        'feedbacks': []
    }
    print(f"New product '{product_name}' added successfully!")

def select_fromProducts(products):
    print("\nSelect a product to give feedback:")
    for product_id, product_data in products.items():
        print(f"{product_id}. {product_data['productName']} - {product_data['productCategory']}")

    while True:
        try:
            selected_id = int(input("Enter the product ID: "))
            if selected_id in products:
                return products[selected_id]
            else:
                print("Invalid product ID. Please try again.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    products = {
        1: {'productName': "Rocking Chair", 'productCategory': "Furniture", 'feedbacks': []},
        2: {'productName': "Dining Table", 'productCategory': "Furniture", 'feedbacks': []},
        3: {'productName': "Chaise Lounge Couch", 'productCategory': "Furniture", 'feedbacks': []},
        4: {'productName': "Corner Book Case", 'productCategory': "Furniture", 'feedbacks': []},
        5: {'productName': "Media Chest Drawer", 'productCategory': "Furniture", 'feedbacks': []},
    }

    customer_account = customerAccount()

    while True:
        print("Welcome to the Product Feedback Management")
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
        print("\nFeedback System Menu:")
        print("1. Provide Feedback")
        print("2. View Feedbacks")
        print("3. Add a New Product")
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
            print("Exiting. Thank you for your feedback!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
