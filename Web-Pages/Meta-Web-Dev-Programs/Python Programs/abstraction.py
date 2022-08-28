from abc import ABC, abstractmethod

class employees(ABC):
    @abstractmethod
    def donate(self):
        pass

class Donate(employees):
    def donate(self):
        amount = input("How much you want to donate? ")
        return amount

amount = list()
john = Donate()
j = john.donate()
amount.append(j)
print(amount)