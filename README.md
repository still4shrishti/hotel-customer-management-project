# Hotel Customer Management System

A command-line hotel management application built in Python using Object-Oriented Programming. Staff can register guests, allocate rooms, manage billing, and generate invoices — all through a simple numbered menu.


## Overview

Small hotels often track guests, rooms, and payments manually using registers or spreadsheets — a process that's slow and error-prone. This project automates those core front-desk tasks in a single, self-contained Python application. All customer data is saved to a text file (`custlist.txt`) so records persist between runs, with no database or network connection required.

## Features

- Add, view, search, and delete customer records
- Allocate and release rooms (10-room inventory, prevents double-booking)
- Calculate bills based on nights stayed and number of guests
- Record payments and track running balance
- Generate a formatted invoice
- Check-out flow that frees the room automatically
- Input validation on every field (name, email, people count, nights, payment amount)
- Data persists across runs via `custlist.txt`

## Technologies Used

- **Python 3** — Object-Oriented Programming (classes, `__init__`, `__str__`, instance methods)
- **File handling** — `open`/`read`/`write` for data persistence
- **`try`/`except`** — input validation and error handling

## Project Structure

```
hotel-management-system/
├── program.py       # Entry point — menu loop, RUN THIS FILE
├── cutsmlist.py     # Customer class + custmanager (Module 1: Customer Management)
├── roommanage.py     # roommanage class (Module 2: Room Management)
├── billings.py       # bill class (Module 3: Billing)
├── data.py           # Save/load customer data to/from custlist.txt
├── test.py           # 8 automated test cases for custmanager
└── custlist.txt       # Data file — auto-created/updated on exit, don't edit manually
```

## Installation

No external libraries are required — only Python 3's standard library is used.

1. Clone the repository:
   ```
   git clone https://github.com/still4shrishti/hotel-customer-management-project.git
   cd hotel-management-system
   ```
2. Make sure Python 3 is installed:
   ```
   python --version
   ```
   That's it — no `pip install` needed.

## How to Run

Open a terminal in the project folder and
RUN
```
python program.py
```

Follow the on-screen menu to add customers, allocate rooms, calculate bills, record payments, and check guests out.

**Note:** Data is only saved to `custlist.txt` when you exit via option `0` from the menu. Closing the terminal window directly or pressing Ctrl+C will not save your changes.

## How to Test
Open a terminal in the project folder and
RUN
```
python test.py
```

This runs 8 automated test cases covering valid/invalid customer input, search, delete, and balance calculation, and prints a `PASSED`/`FAILED` result for each along with a summary.

## Sample Menu

```
========================================
      HOTEL CUSTOMER MANAGEMENT SYSTEM
========================================
1. Add Customer
2. View All Customers
3. Search Customer By ID
4. Delete Customer
5. Show Available Rooms
6. Allocate Room
7. Calculate Bill
8. Record Payment
9. Show Invoice
10. Check Out Customer
0. Exit
```

## Screenshots

**1. Adding a customer and viewing all customers**
<img width="1178" height="892" alt="Screenshot 2026-09-29 191041" src="https://github.com/user-attachments/assets/1c29b5b9-9e09-4107-bfd8-38b2257fde04" />

**2. Allocating a room and calculating a bill**

<img width="971" height="885" alt="Screenshot 2026-09-29 191145" src="https://github.com/user-attachments/assets/791214a3-b3b0-4af0-9286-2008f58c3fde" />

**3. Recording a payment and generating an invoice**
                                             
<img width="745" height="455" alt="Screenshot 2026-09-29 191307" src="https://github.com/user-attachments/assets/34a872dc-b113-40e7-945e-f18eb5eecb8f" />
                                                               PAYMENT RECORD
<img width="812" height="708" alt="Screenshot 2026-09-29 191332" src="https://github.com/user-attachments/assets/5b2305b1-46e6-4833-8367-9e11d9342b3d" />
                                                               INVOICE GENRATING
**4. Running the test suite**

<img width="855" height="493" alt="Screenshot 2026-09-29 191522" src="https://github.com/user-attachments/assets/d6a100b8-00c3-4fcd-8dc2-a69d132d34be" />



