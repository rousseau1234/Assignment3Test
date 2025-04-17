# Assignment3Test
# README – Software Design Principles in My Code

## About This Project

This project is based on my Python programs: `calculator.py`, `discount_calculator.py`, and `greeting.py`. These programs show how good software design principles can be used to make clean, simple, and easy-to-read code. The main goal is not only to make the code work but also to make it easy for others to understand and improve in the future.

## How Design Principles Were Used

### KISS – Keep It Simple, Stupid  
In all my files, I kept the code simple. For example, in `calculator.py`, each operation (add, subtract, multiply, divide) is clearly written in its own function. This makes the code easy to read and understand.

### DRY – Don’t Repeat Yourself  
I avoided writing the same code many times. In `calculator.py`, instead of repeating the math logic, I created functions for each operation. This saves time and makes the code easier to fix or update.

### SRP – Single Responsibility Principle  
Each function has only one job. For example, in `discount_calculator.py`, the `calculate_discount` function only calculates the discount — it does not handle input or output.

### Open/Closed Principle  
The functions can be reused or extended without changing the core logic. If someone wants to add more features, like tax calculations in `discount_calculator.py`, they can do it by adding new functions, not by changing the old ones.

### Composition Over Inheritance  
Even though my code is simple and does not use classes, I still followed this idea by keeping small, reusable functions instead of making one big one.

### Separation of Concerns  
In `greeting.py`, the input and output are separated from the message logic. This makes it easier to change the greeting message or how the user inputs data in the future.

### YAGNI  
I only wrote code that I needed. For example, I didn’t add extra math functions in `calculator.py` that I wasn’t going to use.

### Avoid Premature Optimization  
I made sure the code works first. I didn’t worry about making it faster or shorter before making sure it is correct.

### Refactor and Clean Code  
I reviewed my code often to keep it neat. I also used meaningful names for functions and variables so anyone can understand what they do.

## Conclusion

This project follows software design principles to keep the code clean, easy to read, and ready for future updates.
