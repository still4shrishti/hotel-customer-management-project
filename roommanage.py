class roommanage:
    def __init__(self):
        #how many rooms are there in the hotel
        self.all = ["101", "102", "103", "104", "105",
                           "106", "107", "108", "109", "110"]
    def findrooms(self, customers):
        fill = []
        for c in customers:
            if c.room is not None and not c.checkedout:
                fill.append(c.room)

        availa = []
        for room in self.all:
            if room not in fill:
                availa.append(room)
        return availa

    def allotroom(self, customers, customer, roomnumber):
        roomno= roomnumber.strip()
        available = self.findrooms(customers)

        if roomno not in self.all:
            print(f"error: {roomno} is not a valid room. Choose from: {self.all}")
            return

        if roomno not in available:
            print(f"error: room {roomno} is occupied.")
            return

        customer.room = roomnumber
        print(f"Room {roomnumber} Allocated To {customer.name}.")

    def gone(self, customer):
        customer.room = None
        customer.checkedout = True