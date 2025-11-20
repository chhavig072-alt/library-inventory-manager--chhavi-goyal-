📚 Library Inventory Manager

A modular, object-oriented command-line application to manage a library catalog.

✨ Overview

This project is a lightweight and fully modular Library Inventory Management System designed using Object-Oriented Programming (OOP) principles.
It helps manage a collection of books through a simple and user-friendly CLI (Command Line Interface).

The system supports adding books, issuing and returning them, viewing the entire inventory, searching for books, and saving all data persistently using JSON.

This project fulfills the requirements of the assignment:

“Object-Oriented Design and Robust Programming in a Library Management System”

🧠 Key Features
✅ 1. OOP Class Design (Book & LibraryInventory)

Clean class structure

Encapsulated attributes & methods

Magic methods (__str__)

Functions for issuing, returning, checking availability

✅ 2. Persistent Data Storage (JSON)

Automatically loads catalog at startup

Saves all changes to library_catalog.json

Handles missing or corrupted files safely

✅ 3. Robust Programming

Extensive try-except blocks

Validates all user input

Gracefully handles errors

✅ 4. Logging (INFO & ERROR Levels)

Logs events to library_manager.log

Tracks issues, errors, and all actions

✅ 5. Menu-Driven CLI

A simple and intuitive interface where the user can:

Add a new book

Issue a book

Return a book

View the complete catalog

Search books by title or ISBN

Exit the program

✅ 6. Python Package Structure

The project follows a clean package layout:

library_manager/
│── __init__.py
│── book.py
│── inventory.py
│
└── cli/
    └── main.py

🛠️ How to Run the Application
1. Navigate to the project folder
cd path/to/library-inventory-manager

2. Run the application using module execution

This is important — the CLI must be run as a module:

python -m library_manager.cli.main


If your Python is installed as python3, use:

python3 -m library_manager.cli.main

🧪 Example Output
--- Library Inventory Manager ---
1. Add Book
2. Issue Book
3. Return Book
4. View All Books
5. Search Book
6. Exit
Enter your choice (1-6): 1

--- Add New Book ---
Title: pretty little baby
Author: moonberry
ISBN (unique identifier): 736473
Book 'pretty little baby' added.

--- Issue Book ---
Enter ISBN of the book to issue: 736473
Successfully issued: pretty little baby

--- Return Book ---
Enter ISBN of the book to return: 736473
Successfully returned: pretty little baby

--- Current Catalog ---
1. Title: pretty little baby | Author: moonberry | ISBN: 88578 | Status: Available
2. Title: pretty little baby | Author: moonberry | ISBN: 736473 | Status: Available

--- Search Book ---
Enter search type (1 or 2): 2
Enter ISBN: 88578

--- Search Result (ISBN) ---
Title: pretty little baby | Author: moonberry | ISBN: 88578 | Status: Available

Exiting Library Manager. Goodbye!

📦 Files Included

book.py – Book class

inventory.py – LibraryInventory class

main.py – CLI

library_catalog.json – Persistent storage

library_manager.log – Log file

README.md – Documentation

requirements.txt – Standard library references

test_book.py

test_inventory.py

🌟 Assignment Requirements Covered

✔ OOP class design

✔ File handling with JSON

✔ Exception handling

✔ Logging

✔ Modular CLI

✔ Packaging with __init__.py

✔ Proper folder structure

✔ Documentation

✔ Unit Tests

👩‍💻 Author

Chhavi Goyal
B.Tech (CSE) ai/ml
Programming for Problem Solving using Python
