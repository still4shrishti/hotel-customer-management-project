class bill:
    ratepernight = 1500 
    perperson = 300     

    def calbill(self, customer, nights):
        try:
            nights = int(nights)
        except ValueError:
            print("error: write a valid number of nights.")
            return

        if nights <= 0:
            print("error: nights must be more than 0.")
            return

        extrapeo = max(customer.people - 1, 0)
        total = (self.ratepernight + (extrapeo * self.perperson)) * nights
        customer.due = total
        customer.nights = nights
        print(f"BILL CALCULATED: Rs. {total} for {nights} night(s).")

    def recordpay(self, customer, amount):
        try:
            amo = float(amount)
        except ValueError:
            print("error: payment amount must be a number.")
            return

        if amo < 0:
            print("error: payment cannot be negative.")
            return

        customer.paid += amo
        print(f"PAYMENT RECORDED. Remaining balance: Rs. {customer.balance()}")

    def invoice(self, customer):
        print("----------------------------")
        print("         VIT HOTEL")
        print("         INVOICE")
        print("----------------------------")
        print(f"Customer : {customer.name}")
        print(f"Room     : {customer.room}")
        print(f"Due      : Rs. {customer.due}")
        print(f"Paid     : Rs. {customer.paid}")
        print(f"Balance  : Rs. {customer.balance()}")
        print(f"staying  : {customer.people} person(s)")
        print(f'Nights   : {customer.nights} night(s)')
        print("----------------------------")
        print("Thank you for staying with us!")