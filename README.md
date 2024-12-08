#  Share your Experience: Product Feedback Management

Share your Experience: Product Feedback Management is a Python based console application designed to manage the product feedback based on customer insights or experience. This system allows users to add products and give feedback on a product, the customer feedback has two forms including rating and suggestions. This console application will form a direct connection between customers and companies that will help them improving the quality of their products and  enhancing customer experience. 

 # *Topics Covered*
 
  ***Project Overview*** 

  ***Features***
  
  ***Explanation of How Python Concepts, Libraries, etc were applied***
  
* Programming Languange used
* Object Oriented Programming (OOP)
* Data storage using json
* Control Flow
* String Fromatting
* Error Handling
* re Library
* Data Structures
  
***Details of the chosen SDG and its implementation into the project***

 ***Instruction for running the program***

## **Project Overview**

 Share your Experience: Product Feedback Management is a Python based console application designed to manage the product feedback based on customer insights or experience. This system allows users to add products and give feedback on a product, the customer feedback has two forms including rating and suggestions. This console application will form a direct connection between customers and companies that will help them improving the quality of their products and  enhancing customer experience. 

 ## **Features**
**Account management**
 * Create Account : For the customers that doesnt have an account.
 * Log in: Log in using the existing account.

 **Feedback Management**
 * Provide a Feedback: For displaying the list of the product and proceed in giving feedback.
 * View Feedback: Displaying all of the feedback of the customers including their timestamps.
 * Add a new products: For admin to add product on the list and for the user to add the product if the product they will give feedback are not on the list.
   
## **Explanation of How Python Concepts, Libraries, etc were applied**

 This system entitled `Share your Experience: Product Feedbacks System` uses `Python` as its main programming languange.

#### 1. Object Oriented Programming (OOP)
1.1 **Encapsulation:** The system uses classes `customerAccount` and `Feedback` to encapsulate data functionality. The `customerAccount` class manages user accounts, including creation, login, and data persistence. The password has a requirement for enforcing password complexity; this is done using the`requiredStongPassword` method that uses`re library` for regular expression, and it will hash the password for security of the account using the `argon2 library` . 

The `Feedback` class encapsulates all of the relevant information associated with a feedback entry, including `feedback id`, `user id`, `name`, `feedback`, `rating`, `date` using `timestamp` and using a `datetime library`, and an `optional suggestion`.

1.2 **Abstraction:** In the `customerAccount` class, the account was used in the `passwordHasher,` and the account was managed internally, so the user will only interact with the methods like `create_account` and `login` without worrying how the account was secured or whether the account is stored in the `json` library. In the `Feedback class` abstraction was used to generate `unique IDs` and `timestamps` and determine whether the user will give suggestions based on their ratings. 
 
#### 2. Data Storage using json
2.1 The `json` library is used to store and retrieve customer accounts data in `customerAccounts.json` and product feedbacks  using `customerFeedback.json`.

 This allows  the system to maintain the data's between each sessions. This are the examples on how the cutomer accounts and customer feedbacks was stored in the json library:

**Storing the customer accounts, hashing the password and providing user id.**

![Screenshot 2024-12-06 081634](https://github.com/user-attachments/assets/00d37ed8-9d2b-4ddc-b026-6e836c1ce77e)

**Storing customer feedbacks, inclucing `feedback_id`, `user_id`, `feedback`, `rating`, `suggestion`, and `timestamp`.**

![Screenshot 2024-12-06 081707](https://github.com/user-attachments/assets/0975a1c5-87fd-48c9-81b1-c21e576e9d03)

#### 3. Control Flow

3.1 **Conditional statements:** `(if, elif, else)` help the system for determining the flow based on some conditions to ensure the program behaves according to its conditions.

3.2 **Loops:** Loops like `while` loop is used in many ways in this system, for user account creation until the username is valid,  used in validating inputs until the correct input is given and use in main menu until the user exit the program. While `for` loop  is used to iterate products and feedback for displaying informations and calculating average rating through feedbacks. 

#### 4. String Formatting

4.1 **F-Strings:** F-string was used in this system to provide a concise and convenient way to directly embed variables into string.  

#### 5. Error Handling
5.1 `try` and `except` blocks are used to handle potential errors in the system, prevent the system for crashing  and guide the users using informative messages making the program more robust and user friendly.

5.2 Input validation is used to ensure that user inputs are within the expected ranges.

#### 6. re library

6.1 The `re library` is used in this system to make a complexity  password requirements to ensure that passwords is valid.

![passrequirement](https://github.com/user-attachments/assets/cfb6ff8a-808d-480e-964c-6ea5a5b5b7a8)


#### 7. Data Structures

7.1 **Dictionaries** like `accounts`  is use to store user account infromation containing usernames as their key values that contains `user_id` and `password`. `products` dictionary is used to store informations about products like `productName`, `product_id`, `productCategory`, `feedbacks`,  to allows easy access on a products.

7.2 **Lists:** each products has a dictionary containing a list of feedbacks that stores Feedback objects in `products[product_id]['feedbacks']` and saving feedback details in `json` format. In the main list was used in the products dictionary with an empty feedback list.

## **Details of chosen SDG and its impelentation into the project**

<p align="center">
  <img src="https://github.com/user-attachments/assets/0519de13-09b6-49c6-b7ab-24a00590e52f" alt="giphy" width="200">
</p>


  This Product Feedback Management directly promotes `SDG 12 Responsible Consumption and Production`, by collecting customer insights about the quality of product and for better improvements. The system will encourage sustainable practices by providing manufacturers with actionable data’s given by the users. With the feedback, rating and suggestion provided by the user’s, companies can reduce likelihood the production of low-quality products and avoiding the waste of the items use in making products. It promotes sustainable consumption for the buyer’s, access feedbacks information they can make a right decision choosing high quality products to reduce waste from buying low quality products.

## **Instructions for running the program**

**Step 1: Make sure the argon2 library was installed in the terminal**

![Screenshot 2024-12-06 083905](https://github.com/user-attachments/assets/be771996-391e-43d7-8c4d-bcfe179a520f)

**Login or Create Account**

![Create or Login](https://github.com/user-attachments/assets/624dae8b-b4ae-412b-a5f4-1bf403c0bfb4)

**Step 2: Creating account for new user**

Once the user selected Create Account the user will have to input a new username and a password(must contain atleast one capital letter and one number). After creating the account the user will  see a welcome message.

![Create Account](https://github.com/user-attachments/assets/100c7357-4a16-47cc-b79d-27feba112b48)

**Logging in**

Log in with your excisting account.

![Login](https://github.com/user-attachments/assets/490b6976-befa-4252-8461-7795e23ea04a)

**Product Feedback Menu**

![Menu](https://github.com/user-attachments/assets/c4e6bbe7-fc22-462c-8763-8d90af36111f)

**Step 3: List of Products**

Once the user choose Provide a feedback the list of product names and their category will display


![Choices](https://github.com/user-attachments/assets/4fc3e1e6-175a-4b5a-a3d9-5adff10467ef)

**Step 4: Providing a Feedback**

After the user choose a product, the user will proceed in giving a feedback

![Giving feedback](https://github.com/user-attachments/assets/505748bf-91da-458c-9887-79385a10ab18)

**Provide Suggestion**

If the user rating is less than or equal 2 the system will ask the user if he/she wants to provide a suggestion.

![Suggestion](https://github.com/user-attachments/assets/732b55e8-195d-4024-afc6-68e1e53da040)

**Step 5: Viewing Feedbacks**

After giving feedback the user can view the products that has a feedback


![ViewFeedback](https://github.com/user-attachments/assets/87970319-7dc7-4ee3-b02a-57a541d67f3f)

**Step 6: Adding a Product**

The user who will provide a feedback might add a product with its name and category if he does not find it in the product list displayed.

![Add a product](https://github.com/user-attachments/assets/7c3acbe7-a74d-461f-af40-54d4b5cf210f)

**Step 7: Exiting the System**

If the user has finish giving feedback and exit the program his/her account will automatically log out an will receive a message of appreciation.


![Exit](https://github.com/user-attachments/assets/8dff1e8c-a4df-4723-81b8-6eb56cdbba33)











  
 
