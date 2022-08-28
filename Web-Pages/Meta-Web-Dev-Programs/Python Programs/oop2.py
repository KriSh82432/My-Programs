class paySlips:
    def __init__(self, name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment =  "yes"

    def status(self):
        if self.payment == "yes":
            return self.name+" is paid "+"$"+self.amount
        else:
            return self.name+" is not paid yet"

krishna = paySlips("Krishna", "no", "2500")
subiksha = paySlips("Subiksha", "yes", "2500")

print(krishna.status(),subiksha.status(), sep='\n')

krishna.pay()
print("After payment:")

print(krishna.status(),subiksha.status(), sep='\n')