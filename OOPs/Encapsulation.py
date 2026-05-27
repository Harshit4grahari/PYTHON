#Encapsulation is a process of wrapping data and code together into a single unit. It is one of the fundamental principles of Object-Oriented Programming (OOP). Encapsulation helps to protect the data from unauthorized access and modification by hiding the internal details of an object and only exposing a public interface.
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self.__balance
    
account = BankAccount("Alice", 1000)
account.deposit(500)