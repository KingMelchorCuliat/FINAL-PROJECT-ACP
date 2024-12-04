> #  Share your Experience: Product Feedback System

Share your Experience: Product Feedback system is a Python based tool that allows users to add products and give feedback on a product, this feedback can take forms including rating and suggestions. The main goal of this system is to improve the sustainability of a certain company products by using feedback to identify and address their product weaknesses. 

> # *Topics Covered*
  ***I.*** ***Project Overview*** 
  
  ***II.*** ***Explanation of How Python Concepts, Libraries, etc were applied***
  
* Programming Languange used
* Object Oriented Programming (OOP)
* Data storage using json
* Control Flow
* Stribg Fromatting
* Error Handling
* re Library
* Data Structures
  
 ***III.*** ***Details of the chosen SDG and its implementation into the project***

***IV.*** ***Instruction for running the program***

 ### **I. Project Overview**

 Product Feedback system is a tool that allows users to give feedback on a product, this feedback can take forms including rating and suggestions. The main goal of this system is to improve the sustainability of a certain company products by using feedback to identify and address their product weaknesses

### **II. Explanation of How Python Concepts, Libraries, etc were applied**

#### 1. Programming Languange used
1.1 This system entitled `Share your Experience: Product Feedbacks System` uses `Python` as its main programming languange.

#### 2. Object Oriented Programming (OOP)
2.1 The system uses classes `customerAccount` and `Feedback` to encapsulate data functionality. The `customerAccount` class manages user accounts, including secure password using `argon2` library. The `Feedback` class represents an individual feedback entries, including the time and date when the customer submitted a feedback using `datetime` library.

#### 3. Data Storage using json
3.1 The `json` library is used to store and retrieve customer accounts data in `customerAccounts.json` and product feedbacks  using `customerFeedback.json`. This allows  the system to maintain the data's between each sessions.

#### 4. Control Flow

4.1 Conditional statements: `(if, elif, else)` help the system for determining the flow based on some conditions to ensure the program behaves according to its conditions.

4.2 Loops: Loops like `while` loop is used in many ways in this system, for user account creation until the username is valid,  used in validating inputs until the correct input is given and use in main menu until the user exit the program. While `for` loop  is used to iterate products and feedback for displaying informations and calculating average rating through feedbacks. 

#### 5. String Formatting

5.1 F Strings: F string was used in this system to provide a concise and convenient way to directly embed variables into string.  

#### 6. Error Handling
6.1 `try` and `except` blocks are used to handle potential errors in the system, prevent the system for crashing  and guide the users using informative messages making the program more robust and user friendly.

6.2 Input validation is used to ensure that user inputs are within the expected ranges.

#### 7. re library

7.1 The re library is used in this system to make a complexity  password requirements to ensure that passwords is valid.

#### 8. Data Structures

8.1 Dictionaries like `accounts`  is use to store user account infromation containing usernames as their key valus that contains `user_id` and `password`. `products` dictionary is used to store informations about products like productName, product_id, productCategory, feedbacks,  to allows easy access on a products.

8.2 Lists ech products has a dictionary containing a list of feedbacks that stores Feedback objects.






### **III. Details of chosen SDG and its impelentation into the project**

  This Product Feedback System directly promotes `SDG 12 Responsible Consumption and Production`, by collecting customer insights about the quality of product and for better improvements. The system will encourage sustainable practices by providing manufacturers with actionable data’s given by the users. With the feedback, rating and suggestion provided by the user’s, companies can reduce likelihood the production of low-quality products and avoiding the waste of the items use in making products. It promotes sustainable consumption for the buyer’s, access feedbacks information they can make a right decision choosing high quality products to reduce waste from buying low quality products.

### **IV. Instructions for running the program**

**Login or Create Account**

![Create or Login](https://github.com/user-attachments/assets/624dae8b-b4ae-412b-a5f4-1bf403c0bfb4)

**Creating account for new user**

Once the user selected Create Account the user will have to input a new username and a password(must contain atleast one capital letter and one number). After creating the account the user will  see a welcome message.

![Create Account](https://github.com/user-attachments/assets/77382060-c3e7-4110-8442-07ee4036eaa2)

**Logging in**

Log in with your excisting account.

![Login](https://github.com/user-attachments/assets/490b6976-befa-4252-8461-7795e23ea04a)

**Product Feedback Menu**

![Menu](https://github.com/user-attachments/assets/c4e6bbe7-fc22-462c-8763-8d90af36111f)

**List of Products**

Once the user choose Provide a feedback the list of product names and their category will display


![Choices](https://github.com/user-attachments/assets/4fc3e1e6-175a-4b5a-a3d9-5adff10467ef)

**Providing a Feedback**

After the user choose a product, the user will proceed in giving a feedback

![Giving feedback](https://github.com/user-attachments/assets/505748bf-91da-458c-9887-79385a10ab18)

**Provide Suggestion**

If the user rating is less than or equal 2 the system will ask the user if he/she wants to provide a suggestion.

![Suggestion](https://github.com/user-attachments/assets/732b55e8-195d-4024-afc6-68e1e53da040)

**Viewing Feedbacks**

After giving feedback the user can view the products that has a feedback


![ViewFeedback](https://github.com/user-attachments/assets/87970319-7dc7-4ee3-b02a-57a541d67f3f)

**Adding a Product**

The user who will provide a feedback might add a product with its name and category if he does not find it in the product list displayed.

![Add a product](https://github.com/user-attachments/assets/7c3acbe7-a74d-461f-af40-54d4b5cf210f)

**Exiting the System**

If the user has finish giving feedback and exit the program his/her account will automatically log out an will receive a message of appreciation.


![Exit](https://github.com/user-attachments/assets/8dff1e8c-a4df-4723-81b8-6eb56cdbba33)











  
 
