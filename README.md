# Requisition System Project

I have developed this Python program to collect staff data like name, staff ID, name of their purchased items and the price. Based on the total amount of purchase, the system will automatically decide the status of the requisition. A new requisiton with an unique requisition number will be created each time for new entries. This code was designed following the basic software design principles which are outlined below.
# KISS (Keep It Simple, Stupid)

I have tried to keep my code as simple as possible. The functions named staff_info(), requisitions_total(), requisition_approval() and display_requisitions() are used to simply collecting the staff informations, adding up the total amount of items purchased, approving the requisitons based on the approval threshold of $500 and showing the status of the requisitions respectively. The code is very easier to run and operate, avoiding all sorts of complexities.

# DRY (Don't Repeat Yourself)

Throughout the entire coding, I have avoid using the same code more than once. I have created multiple functions to do the tasks accurately. The dictionaries have been created so that datas are stored and can be used as many times without repeating them which ensures the DRY principle. 

# Open/Closed Principle

As I have tried to keep my codes in module form, any further changes like adding new requisitions, modifying the codes or setting up some new functionalities can be easily done without altering the existing code. The Open/Closed principle is meant to keep the system open to extension but closed to modification, which perfectly aligns with my code.

# Composition Over Inheritance

In this project the functions like staff_info(), requisitions_total(), requisition_approval() and display_requisitions() are used to collect staff data, collect items and total the price, figure out the status of the requisitions and display the final information respectively. So it clearly indicates that my functions are built on top of the other like one function is put inside another, using their return values from the previous one rather than copying the entire thing. This is the way I have maintained this principle.

# Single Responsibility Principle

Since each function of my code is doing single task like the staff_info() is taking the staff data, the requisitions_total() is taking the name of their purchased items and calculating the total, the requisition_approval() is giving a decision on the requisition based on the threshold of $500 and finally the display_requisitions() is showing the final outcome it is obvious that my code has maintained the Single Responsibility principle accurately.

# Separation of Concerns

Separating each functionality of the code has been taken under high consideration by me. I have ensured that each functions are running single task at the same time without overlapping the other functions. For instance, while taking new entries each time the function is not affecting on the existing functions or the informations as they are done separately. 

# YAGNI (You Ain't Gonna Need It)

I have kept all unnecessary functions outside of the system to ensure smooth navigating system, creating better opportunities for future developments. Based on the requirements, I only have included the functions which are needed to run the system without any disturbance. So the code is less complex and easier to understand.

# Avoid Premature Optimisation

Since the code is running smoothly without any issues so far, I am not thinking about optimizing the code at the moment. Though the code has been written simply, it is accurate and running quiet fast as well. Optimizing the code now will be too soon which may make it faster than what it is now, however, it could make the code confusing and harder to fix any issues in future.

# Refactor, Refactor, Refactor

Instead of writing the code in one big function, I have broken it down into small functions like staff_info(), requisitions_total(), requisition_approval() and display_requisitions(), which have made the code easier to navigate, and established a solid example of refactoring principle.

# Clever Code

I firmly believe that, good codes are those which are easier to understand. In my code, I have tried my best to keep it understandable by avoiding unnecessary complexities. The code is properly documented with titles, function names, making it simple and straightforward. 

# Conclusion

To conclude, the python function developed by me perfectly aligns with the software development design principles. The main focus of these principles are keeping the code easy, smart and efficient. These principles will ensure the durabilty of the system by maintaining and keeping it up to date based on the demand over the course of time.
