class Customer:
    def __init__(self, id, name, people, email):
        self.id = id
        self.name = name
        self.people = people
        self.email = email
        self.room = None
        self.due = 0
        self.paid = 0
        self.checkedout = False
        self.nights = 0
    def __str__(self):
        status = "Checked out" if self.checkedout else "Staying"
        return f"ID {self.id} | {self.name} | Email: {self.email} | People: {self.people} | Room: {self.room} | Due: Rs. {self.due} | Paid: Rs. {self.paid} | {status}"

    def balance(self):
        return self.due - self.paid

class custmanager:
    def __init__(self):
        self.customers = []

    def addcust(self, name, people, email):
        name = name.strip()
        email = email.strip()

        if name == "":
            print("error: write your name.")
            return

        if "@" not in email or "." not in email:
            print("error: write a valid email.")
            return

        try:
            people = int(people)
        except ValueError:
            print("error: write a valid number.")
            return

        if people <= 0:
            print("error: write a valid number of people if only one is staying write 1.")
            return

        newid = len(self.customers) + 1
        customer = Customer(newid, name, people, email)
        self.customers.append(customer)
        print(f"Customer added successfully with ID {newid}.")

    def viewcust(self):
        if len(self.customers) == 0:
            print("No customers found.")
            return
        print(f"Total customers: {len(self.customers)}")
        for c in self.customers:
            print(c)

    def searchcust(self, customerid):
        for c in self.customers:
            if c.id == customerid:
                return c
        return None

    def deletecust(self, customerid):
        customer = self.searchcust(customerid)
        if customer:
            self.customers.remove(customer)
            print("Customer deleted successfully.")
        else:
            print("No customer found with that ID.")
