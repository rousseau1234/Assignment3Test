# Requisition System Project

I have developed this Python program to collect staff data like name, staff ID, name of their purchased items and the price. Based on the total amount of purchase, the system will automatically decide the status of the requisition. A new requisiton with an unique requisition number will be created each time for new entries. This code was designed following the basic software design principles which are outlined below.
## KISS (Keep It Simple, Stupid)

I have tried to keep my code as simple as possible. The functions named staff_info(), requisitions_total(), requisition_approval() and display_requisitions() are used to simply collecting the staff informations, adding up the total amount of items purchased, approving the requisitons based on the approval threshold of $500 and showing the status of the requisitions respectively. The code is very easier to run and operate, avoiding all sorts of complexities.

## DRY (Don't Repeat Yourself)

Throughout the entire coding, I have avoid using the same code more than once. I have created multiple functions to do the tasks accurately. The dictionaries have been created so that datas are stored and can be used as many times without repeating them which ensures the DRY principle. 

## Open/Closed Principle

As I have tried to keep my codes in module form, any further changes like adding new requisitions, modifying the codes or setting up some new functionalities can be easily done without altering the existing code. The Open/Closed principle is meant to keep the system open to extension but closed to modification, which perfectly aligns with my code.

## Composition Over Inheritance

In this project the functions like staff_info(), requisitions_total(), requisition_approval() and display_requisitions() are used to collect staff data, collect items and total the price, figure out the status of the requisitions and display the final information respectively. So it clearly indicates that my functions are built on top of the other like one function is put inside another, using their return values from the previous one rather than copying the entire thing. This is the way I have maintained this principle.

## Single Responsibility Principle

Since each function of my code is doing single task like the staff_info() is taking the staff data, the requisitions_total() is taking the name of their purchased items and calculating the total, the requisition_approval() is giving a decision on the requisition based on the threshold of $500 and finally the display_requisitions() is showing the final outcome it is obvious that my code has maintained the Single Responsibility principle accurately.

## Separation of Concerns

Separating each functionality of the code has been taken under high consideration by me. I have ensured that each functions are running single task at the same time without overlapping the other functions. For instance, while taking new entries each time the function is not affecting on the existing functions or the informations as they are done separately. 

## YAGNI (You Ain't Gonna Need It)

I have kept all unnecessary functions outside of the system to ensure smooth navigating system, creating better opportunities for future developments. Based on the requirements, I only have included the functions which are needed to run the system without any disturbance. So the code is less complex and easier to understand.

## Avoid Premature Optimisation

The principle of **Avoid Premature Optimisation** is followed by initially getting the system working and optimizing performance later. Functions like `submit_requisition()`, `respond_requisition()`, and `requisition_statistics()` are kept simple. Once the system is working, performance can be profiled and optimised if required.

## Refactor, Refactor, Refactor

In this project, functions like `submit_requisition()` and `respond_requisition()` can be optimized and made more readable. Small things, such as simplifying logic or organizing code, accumulate in the long run.

## Clever Code

Code should be readable, not clever or confusing. In this project, all functions are written in plain code so others can view and modify it easily. Smart-looking one-liners or shortcuts are not used.

## Conclusion

This Requisition System demonstrates the application of basic software design principles in the sense that the code is neat, easy to maintain, and expandable. KISS, DRY, Open/Closed, Single Responsibility, Separation of Concerns, and YAGNI principles are applied in order to make the system efficient, understandable, and extensible in future if needed.
