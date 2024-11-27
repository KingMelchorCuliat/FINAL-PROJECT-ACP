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

### **II. Explanation of How Python Concepts, Libararies, etc were applied**

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

8.1 Dictioanires like `accounts`  is use to store user account infromation containing usernames as their key valus that contains `user_id` and `password`. `products` dictionary is used to store informations about products like productName, product_id, productCategory, feedbacks,  to allows easy access on a products.

8.2 Lists ech products has a dictionary containing a list of feedbacks that stores Feedback objects.






### **III. Details of chosen SDG and its impelentation into the project**

  This Product Feedback System directly promotes `SDG 12 Responsible Consumption and Production`, by collecting customer insights about the quality of product and for better improvements. The system will encourage sustainable practices by providing manufacturers with actionable data’s given by the users. With the feedback, rating and suggestion provided by the user’s, companies can reduce likelihood the production of low-quality products and avoiding the waste of the items use in making products. It promotes sustainable consumption for the buyer’s, access feedbacks information they can make a right decision choosing high quality products to reduce waste from buying low quality products.

### **IV. Instructions for running the program**

**Login or Create Account**

![Create or Login](https://github.com/user-attachments/assets/624dae8b-b4ae-412b-a5f4-1bf403c0bfb4)


**Creating account for new user**











  
 
