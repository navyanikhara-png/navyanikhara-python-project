# Library Management System (Python)
Overview

The Library Management System is a Python-based console program that allows users to manage a small collection of books. It supports basic functions such as adding new books, displaying available books, borrowing books, and returning books.

This project demonstrates the use of Object-Oriented Programming (OOP) in Python, including classes, objects, and methods.

 Features

 Add Books (with unique Book ID, title, author, and number of copies)

Display All Books

 Borrow Books (checks availability before borrowing)

 Return Books

Auto-update number of copies

 Prevents borrowing when no copies are available

 Easy console-based interface

 Technologies Used

Python 3.x

Object-Oriented Programming (OOP)

Project Structure
Library-Management-System/
│
├── library_management.py     # Main Python program
├── README.md                 # Documentation file
└── report.md / report.pdf    # Project report (optional)

 How to Run the Program

Install Python 3.8 or higher.

Download or copy library_management.py.

Open a terminal or command prompt.

Run the program:

python library_management.py

 Example Interaction
========== Library Management System ==========
1. Add Book
2. Display Books
3. Borrow Book
4. Return Book
5. Exit
Enter your choice: 1
Enter Book ID: B101
Enter Book Title: Python Basics
Enter Author: John Doe
Enter number of copies: 3
Book added successfully!

 Concepts Used

Classes & Objects

Dictionaries

Control flow (loops, conditionals)

String formatting

Input/output handling

 Future Improvements

Add user login system

Store books in a database (SQLite/MySQL)

GUI version (Tkinter / PyQt)

Due date & fine management

Export book data to CSV or JSON
