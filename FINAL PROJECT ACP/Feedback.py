import datetime # This library is used for displaying the date when the feedback is submitted
import json

#Class for managing customer Feedbacks
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
                print("Thank you for your suggestion! We will promise to improve our product for customer satisfaction.")

def load_customerFeedback(filename='customerFeedback.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Feedback file not found. Creating a new one.")
        return {}

def save_customerFeedback(products, filename='customerFeedback.json'):
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
