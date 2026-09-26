# Problem Statement

Small hotels manage check-ins, room allocation, and billing manually using 
registers or spreadsheets. This is slow, error-prone, and makes it hard to 
track room occupancy or how much a guest owes.

# Scope of the Project

A command-line hotel management system that automates the core front-desk tasks:
- Registering guests
- Assigning and releasing rooms
- Calculating bills and recording payments
- Producing invoices at checkout

Designed for a single property with a fixed set of 10 rooms. No networking, 
database server, or multi-user login — runs as a local, single-user application.

# Target Users

- Hotel front-desk staff who need a fast way to log guests and manage rooms
- Small hotel/guesthouse owners without budget for commercial hotel software

# High-Level Features

1. **Customer Management** — add, view, search, and delete guest records
2. **Room Management** — check availability, allocate rooms, prevent double-booking
3. **Billing** — calculate stay cost, record payments, generate an invoice, track balance
4. Data is saved to `custlist.txt` so records aren't lost when the program closes
