"""
1. Bank Account Management System
"""

class Bank_account:
    def __init__(self, acc_holder, balance):
        self.acc_holder=acc_holder
        self.balance=balance
    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited Rs.{amount} and new balance is Rs.{self.balance}")
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew Rs.{amount} and new balance is Rs.{self.balance}")
        else:
            print("Insufficient funds")
    def display_info(self):
        print(f"Account Holder: {self.acc_holder}, Balance: {self.balance}")

holder=(input("Enter the name of the acc holder: "))
initial_balance=int(input("Enter the initial balance: "))

acc=Bank_account(holder, initial_balance)
acc.display_info()

dep_amt, with_amt = map(int,input("Enter deposit amount and withdrawal amount separated by space: ").split())

acc.deposit(dep_amt)
acc.withdraw(with_amt)
