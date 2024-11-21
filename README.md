> # *Product Feedback System*

Product Feedback system is a Python based tool that allows users to give feedback on a product, this feedback can take forms including rating and suggestions. The main goal of this system is to improve the sustainability of a certain company products by using feedback to identify and address their product weaknesses. 

> # *Topics Covered*
  ***I.*** ***Project Overview*** 
  
  ***II.*** ***Explanation of How Python Concepts, Libraries, etc were applied***
 
* Object Oriented Programming (OOP)
* Libraries
* Data Structures
* Error Handling
  
 ***III.*** ***Details of the chosen SDG and its implementation into the project***

***IV.*** ***Instruction for running the program***

 ### **I. Project Overview**

 Product Feedback system is a tool that allows users to give feedback on a product, this feedback can take forms including rating and suggestions. The main goal of this system is to improve the sustainability of a certain company products by using feedback to identify and address their product weaknesses

### **II. Explanation of How Python Concepts, Libararies, etc were applied**

#### 1. Object Oriented Programming (OOP)

1.1 Encapsulation and Classes: Classes like `FeedbackAccount` , `Guest` and  `Feedback` are applied in this system, each of the classes has their own attributes and method to define their use encapsulating data in the `FeedbackAccount` class using dictionary accounts encapsulates within the user interact through methods like `createAccount()` and `login()` and  in the `Feedback` class encapsulate feedback details like name, feedback and rating using the method `userSuggestion()`.

1.2 Instance attributes:  instance attribute like `self.accounts` in `FeedbackAccount` and `self.name`, `self.feedback`, `self.rating` and `self.suggestion` in `Feedback` are used to store objects specific data’s. 


#### 2. Libraries

2.1 Import datetime: library is used to capture the current date using `self.timestamp = datetime.datetime.now() and to get the format yy-dd-mm using timestamp =
feedback.timestamp.strftime('%Y-%m-%d' %H:%M:%S')` to know when and what time the  feedback is provided. Allowing to track when the user gives feedback to the product.

2.2 Import json: this library was used to store the user accounts inclucing username and password and Customer feedback including rating and suggestions.


#### 3. Control Flow

3.1 Conditional statements: `(if, elif, else)` help the system for determining the flow based on some conditions to ensure the program behaves according to its conditions.

3.2 Loops: Loops like `while` loop is used in many ways in this system, for user account creation until the username is valid,  used in validating inputs until the correct input is given and use in main menu until the user exit the program. While `for` loop  is used to iterate products and feedback for displaying informations and calculating average rating through feedbacks. 

#### 4. Data Structures
4.1 Dictionaries: dictionaries like `accounts` are used to manage user accounts efficiently in the `FeedbackAccounts` storing `usernames` as their key and `password` for corresponding values, next is  `products` are use to store product informations like their `names`, `category` and their `feedbacks` where products has its own unique IDs and `Feedbacks` are used for each product are stored in a list within the `product` dictionary for easy iteration and `Feedback` storage in json are used to save data for each product in `userFeedback.json`.

4.2 List: Each of its `product` in a product dictionary has a key called `feedbacks` which hold the list of `Feedback` objects allowing an easy storing of feedback data and `Feedback` data on a json is used to store a list format within the `products` dictionary such as `names`, `rating`, `suggestions` and `timestamp`.

#### 5. String Formatting

5.1 F Strings: F string was used in this system to provide a concise and convenient way to directly embed variables into string.  

#### 6. Error Handling

6.1 Input Validation: check ensure that invalid inputs are handled carefully.

6.2 Feedback Access: ensuring the access of feedback details in the `view_feedbacks` function using if `'feedbacks'` in `productData` and `productData['feedbacks']:`

6.3 Exception Handling: used to manage the unexpected errors to occur and ensuring that the program is user friendy. Handling missing files and invalid inputs using clear error messages to guide the users  such as entering `productId` or feedback `ratings`.

### **III. Details of chosen SDG and its impelentation into the project**

  This Product Feedback System directly promotes `SDG 12 Responsible Consumption and Production`, by collecting customer insights about the quality of product and for better improvements. The system will encourage sustainable practices by providing manufacturers with actionable data’s given by the users. With the feedback, rating and suggestion provided by the user’s, companies can reduce likelihood the production of low-quality products and avoiding the waste of the items use in making products. It promotes sustainable consumption for the buyer’s, access feedbacks information they can make a right decision choosing high quality products to reduce waste from buying low quality products.

### **IV. Instructions for running the program**

**Login or Create Account**


**Creating account for new user**











  
 
