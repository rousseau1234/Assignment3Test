# Requisition System Project

This project is a simple Requisition System built in Python to handle requisitions within an organization. The system allows staff members to submit requisitions, manager to respond to pending requisitions, display requisitions, and view requisition statistics. Below is an overview of the functionality and features of the code.

## KISS (Keep It Simple, Stupid)

The code is based on the **KISS** principle as it has simple and easy-to-understand logic. Each function is designed to perform one task. For example, the `submit_requisition()` function handles submitting the process, and the `display_requisitions()` function displays the submitted requisitions. It makes the system easy to maintain and update. In addition, the design does not include any complexity, which allows other developers working in the future to easily understand and make modifications to the code whenever necessary.

## DRY (Don't Repeat Yourself)

During the project, the **DRY** principle is implemented to prevent redundancy. The `staff_info()` function is implemented in the `submit_requisition()` as well as in the `respond_requisition()` function to retrieve staff information to avoid repetition. Additionally, the calculation of the total cost of requisitions is placed within the `requisitions_details()` function so that when the calculation logic changes, this modification will be carried out at one location only. This reduces the possibilities for mistakes and makes the code easy to maintain.

## Open/Closed Principle

The **Open/Closed** principle is used by keeping the system open to extension but closed to modification. For instance, when additional features are to be added, such as adding additional requisition categories or modifying approval procedures, they are added without altering the main code. The operations are in module form, and new functionality, such as different kinds of items or new approval rules, can be added by adding new functions or classes rather than changing the existing ones.

## Composition Over Inheritance

The system follows the **Composition over Inheritance** principle by keeping all the tasks in one class instead of using many related classes. Each function like `submit_requisition()` or `respond_requisition()` does a specific task. This keeps the code tidy, simple to change, and easy to add new features in the future without turning the code messy or complex.

## Single Responsibility Principle

Each function and class within the system follows the **Single Responsibility Principle**, performing one specific task. For example, the `submit_requisition()` function performs the task of submitting a requisition only, while the `respond_requisition()` function handles the manager's response to pending requisitions. With responsibilities divided, the system is easier to maintain and has less room for error. Each part of the system is handling one specific item, and therefore the code is easier to understand and modify.

## Separation of Concerns

The code is also in compliance with the **Separation of Concerns** principle as it keeps various elements of the system not overlapping in functionality. For example, staff details are handled separately from the requisition details. Requisition submission logic is separated from the approval/rejection logic. This modular design makes it easy to manage and scale the system as new features can be added without affecting the existing functionalities.

## YAGNI (You Ain't Gonna Need It)

The **YAGNI** principle is applied throughout the project by not adding unnecessary complexity. Features are added only when they are needed. For instance, the system does not contain unnecessary features that are not demanded by the core requisition process. By this principle, the system remains easy to navigate, with no unused features or unnecessary code.

## Avoid Premature Optimisation

The principle of **Avoid Premature Optimisation** is followed by initially getting the system working and optimizing performance later. Functions like `submit_requisition()`, `respond_requisition()`, and `requisition_statistics()` are kept simple. Once the system is working, performance can be profiled and optimised if required.

## Refactor, Refactor, Refactor

In this project, functions like `submit_requisition()` and `respond_requisition()` can be optimized and made more readable. Small things, such as simplifying logic or organizing code, accumulate in the long run.

## Clever Code

Code should be readable, not clever or confusing. In this project, all functions are written in plain code so others can view and modify it easily. Smart-looking one-liners or shortcuts are not used.

## Conclusion

This Requisition System demonstrates the application of basic software design principles in the sense that the code is neat, easy to maintain, and expandable. KISS, DRY, Open/Closed, Single Responsibility, Separation of Concerns, and YAGNI principles are applied in order to make the system efficient, understandable, and extensible in future if needed.
