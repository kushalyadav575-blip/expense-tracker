# Expense Tracker

A simple command-line expense tracker built with Python.

The application allows you to record expenses, organize them by category,
track recurring expenses, and generate basic spending reports. Expenses are
saved to a JSON file so they can be loaded again when the program is restarted.

## Features

- Add regular expenses
- Add recurring expenses
- List all recorded expenses
- Calculate total spending by category
- Calculate total spending
- Find the category with the highest spending
- Filter expenses by category
- Store expenses in a JSON file
- Load previously saved expenses when the program starts
- Custom exceptions for invalid expense amounts

## Project Structure

expense-tracker/
│
├── main.py          # Command-line interface
├── expense.py       # Expense and RecurringExpense classes
├── reports.py       # Spending calculations and filtering
├── storage.py       # Saving and loading expenses
├── expenses.json    # Stored expense data
└── README.md

How It Works
The program provides a menu in the terminal:
1. Add expense
2. Add recurring expense
3. List all expenses
4. Show total by category
5. Show total spent
6. Show top category
7. Filter by category
8. Save & quit
Expenses are represented using the Expense class, while recurring expenses
extend it through the RecurringExpense class.  
The application uses JSON for persistent storage. Expenses are converted to
dictionaries when saved and reconstructed as Python objects when loaded.  storage.pyPY
Reports
The tracker can calculate:
Total spending by category
Total spending overall
Monthly spending
Highest-spending category
Expenses belonging to a specific category
These operations are implemented in reports.py. reports.pyPY
Error Handling
The project defines custom exceptions for invalid expense amounts and catches
invalid amount input when adding expenses. expense.pyPY main.pyPY
Requirements
Python 3.x
No external Python packages are required.
Running the Program
Clone the repository and run:
python main.py
The program will load existing expenses from expenses.json if available.
What I Practiced
This project was built to practice Python concepts including:
Classes and inheritance
Custom exceptions
Modules
File I/O
JSON serialization/deserialization
datetime
List comprehensions
Functions and generators
Basic separation of concerns

### One thing I'd change from your current project

I **wouldn't mention `rough.py` in the README**. Its contents are a separate decorator experiment and don't appear to be part of the expense-tracker functionality. fileciteturn0file6L1-L15

Also, your `.gitignore` currently ignores `__pycache__/`, which is exactly what you want. fileciteturn0file0L1-L1

This README is also appropriately **not overdone** for a student project. You're better off with a clean