from cutsmlist import Customer

fil= "custlist.txt"


def savecust(customers):
    file = open(fil, "w")
    for c in customers:
        line = f"{c.id}|{c.name}|{c.people}|{c.email}|{c.room}|{c.due}|{c.paid}|{c.checkedout}\n"
        file.write(line)
    file.close()


def custdata():
    customers = []
    try:
        file = open(fil, "r")
    except FileNotFoundError:
        return customers
    next(file) 
    for line in file:
        parts = line.strip().split("|")
        customer = Customer(
            id=int(parts[0]),
            name=parts[1],
            people=int(parts[2]),
            email=parts[3]
        )
        customer.room = None if parts[4] == "None" else parts[4]
        customer.due = float(parts[5])
        customer.paid = float(parts[6])
        customer.checkedout = parts[7] == "True"
        customers.append(customer)

    file.close()
    return customers