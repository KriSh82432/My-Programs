from abc import ABC, abstractmethod

class Bank(ABC):
    def basicinfo():
        print("This is a generic bank")
        return "Generic bank: 0"
    @abstractmethod
    def withdraw():
        pass


class Swiss(Bank):
    def __init__(self) -> None:
        self.bal = 1000

    def basicinfo(self):
        print("This is the Swiss Bank")
        return "Swiss Bank: "+str(self.bal)

    def check_bal(self):
        print("Your current balance is $"+str(self.bal))
        return self.bal

    def deposit(self, depositAmount):
        print("You made a request to deposit: $"+str(depositAmount))
        self.bal += depositAmount
        print("Your new balance is $"+str(self.bal))
        return self.bal
        
    def withdraw(self, amount):
        print("You made a request to withdraw: $"+str(amount))
        if (self.bal >= amount):
            self.bal -= amount
            print("Withdrawn amount: $"+str(amount) +
                  "\nNew Balance: $"+str(self.bal))
            return self.bal
        else:
            print("Insufficient funds.\nYour balance is "+str(self.bal))
            return self.bal


def main():
    assert issubclass(Bank, ABC), "Bank must derive from class ABC"
    s = Swiss()
    print(s.basicinfo())
    print(Swiss.mro())
    main1()


def main1():
    s = Swiss()
    fn = int(
        input("What do you want to do?\n1. Check balance\n2. Deposit\n3. Withdraw\n"))
    match fn:
        case 1:
            s.check_bal()
        case 2:
            y = int(input("Enter the amount to deposit: "))
            if y > 0:
                s.deposit(y)
            else:
                y = int(input("Enter the amount to deposit: "))
        case 3:
            x = int(input("Enter the amount to withdraw: "))
            if x > 0:
               s.withdraw(x)
            else:
               x = input("Enter the amount to withdraw: ")
        case _:
            print("Invalid input. Try Again (:")
            main1()


if __name__ == "__main__":
    main()
