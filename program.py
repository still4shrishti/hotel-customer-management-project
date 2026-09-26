from cutsmlist import custmanager
from roommanage import roommanage
from billings import bill
import data

cm = custmanager()
cm.customers = data.custdata()   

rm = roommanage()
bm = bill()

MENU = """
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
"""

while True:
    print(MENU)
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("enter customer name: ")
        people = input("enter number of people(INCLUDING YOU): ")
        email = input("enter customer email: ")
        cm.addcust(name, people, email)

    elif choice == "2":
        cm.viewcust()

    elif choice == "3":
        cid = int(input("enter customer ID: "))
        result = cm.searchcust(cid)
        print(result if result else "NO customer found with that ID.")

    elif choice == "4":
        cid = int(input("enter customer ID: "))
        cm.deletecust(cid)

    elif choice == "5":
        print("AVAILABLE ROOMS:", rm.findrooms(cm.customers))

    elif choice == "6":
        cid = int(input("enter customer ID: "))
        customer = cm.searchcust(cid)
        if customer:
            room = input("enter room number to allocate: ")
            rm.allotroom(cm.customers, customer, room)
        else:
            print("NO customer found with that ID.")

    elif choice == "7":
        cid = int(input("enter customer ID: "))
        customer = cm.searchcust(cid)
        if customer:
            nights = input("enter number of nights: ")
            bm.calbill(customer, nights)
        else:
            print("NO customer found with that ID.")

    elif choice == "8":
        cid = int(input("enter customer ID: "))
        customer = cm.searchcust(cid)
        if customer:
            amount = input("enter payment amount: ")
            bm.recordpay(customer, amount)
        else:
            print("NO customer found with that ID.")

    elif choice == "9":
        cid = int(input("enter customer ID: "))
        customer = cm.searchcust(cid)
        if customer:
            bm.invoice(customer)
        else:
            print("NO customer found with that ID.")

    elif choice == "10":
        cid = int(input("enter customer ID: "))
        customer = cm.searchcust(cid)
        if customer:
            rm.gone(customer)
            print(f"{customer.name} checked out.")
        else:
            print("NO customer found with that ID.")

    elif choice == "0":
        data.savecust(cm.customers)
        print("DATA SAVED. Goodbye!")
        break

    else:
        print("INVALID CHOICE, try again.")