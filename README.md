> # *Product Feedback System*

Product Feedback system is a Python based tool that allows users to give feedback on a product, this feedback can take forms including rating and suggestions. The main goal of this system is to improve the sustainability of a certain company products by using feedback to identify and address their product weaknesses. 

> # *Topics Covered*
  ***I.*** ***Project Overview*** 
  
  ***II.*** ***Explanation of How Python Concepts, Libararies, etc were applied***
 
* Object Oriented Programming (OOP)
* Libraries
* Data Structures
* Error Handling
  
 ***III.*** ***Details of the chosen SDG and its implementation into the project***

***IV.*** ***Instruction for running the program***

 ### ***Project Overview***

 Product Feedback system is a tool that allows users to give feedback on a product, this feedback can take forms including rating and suggestions. The main goal of this system is to improve the sustainability of a certain company products by using feedback to identify and address their product weaknesses

### ***Explanation of How Python Concepts, Libararies, etc were applied***

#### 1. Object Oriented Programming (OOP)

1.1 Encapsulation and Classes: Classes like FeedbackAccount , Guest and  Feedback are applied in this system, each of the classes has their own attributes and method to define their use encapsulating data in the FeedbackAccount class using dictionary accounts encapsulates within the user interact through methods like createAccount() and login() and  in the Feedback class encapsulate feedback details like name, feedback and rating using the method userSuggestion(). While the Guest class is used for the user that don’t want to create an account and giving a welcome message.

1.2 Instance attributes:  instance attribute like self.accounts in FeedbackAccount and self.name, self.feedback, self.rating and self.suggestion in Feedback are used to store obects specific data’s. 


#### 2. Libraries

2.1 Import datetime: library is used to capture the current date using self.timestamp = datetime.datetime.now() and to get the format yy-dd-mm using timestamp =
feedback.timestamp.strftime('%Y-%m-%d') to know when feedback is provided. Allowing to track when the user gives feedback to the product.

2.2 Import json: this library was used to store the user accounts inclucing username and password and Customer feedback including rating and suggestions




  
 
