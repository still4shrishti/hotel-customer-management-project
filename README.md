# hotel-customer-management-project

## Overview
A command-line hotel management system built in Python using OOP. Staff can 
register guests, allocate rooms, and manage billing through a simple menu.

## Features
- Add, view, search, and delete customer records
- Allocate and drop rooms (10 rooms, prevents double-booking)
- Calculate bills based on nights stayed and number of guests
- Record payments and track balance
- Generate an invoice
- Check-out flow that frees the room
- Data saved to `custlist.txt` so records persist between runs

## Technologies Used
- Python 3 (OOP: classes, `__init__`, `__str__`, methods)
- File handling for data persistence
- `try`/`except` for input validation

## Project Structure

hotel-management-system/

├── program.py # Entry point - **RUN THIS FILE

├── cutsmlist.py # Customer class + custmanager (Module 1)

├── roommanage.py # roommanage class (Module 2)

├── billings.py # bill class (Module 3)

├── data.py # Save/load customer data

├── test.py # Test cases for custmanager

└── custlist.txt # Data file (auto-created/updated, don't edit manually)  **IT WILL AUTOMATICALLY CREATES WHEN U EXIT THE PROGRAM 


(custlist.txt WILL NOT SAVE OR CREATE IF YOU DON'T EXIT )


## How to Run
python program.py OR run the program.py

Follow the on-screen menu to manage customers, rooms, and billing.

## How to Test to know is everything is going fine?

python test.py OR run test.py

Runs 8 test cases (valid/invalid input for add, search, delete, balance) and 
prints a PASSED/FAILED .




