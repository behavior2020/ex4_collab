"""
Your task is to create a Python program that simulates a simple bank system with the following
functionalities:
● Account Creation
    ○ A function to create a new account with a unique account ID and initial balance.
● Balance Inquiry
    ○ A function to check the current balance of a given account ID.
● Deposit
    ○ A function to deposit an amount to a specific account, updating the balance.
● Withdrawal
    ○ A function to withdraw an amount from a specific account, updating the balance if
sufficient funds exist.
● Account Summary
    ○ A function to print a summary of an account, including the account ID and current
balance.
"""
import random


class Banking:
    def __init__(self, account_id, balance):
        # accounts = {}
        self.account_id = account_id
        self.balance = balance

    def account_creation(self):
        """creates a new account with a unique account ID and initial balance."""
        self.account_id = random.randint(10000000, 99999999)
        # self.accounts[account_id] = 0
        self.balance = 0
        return f"Account ID: {self.account_id}\nBalance: {self.balance}"

    def balance_inquiry(self, account_id):
        """checks the current balance of a given account ID."""
        # balance = self.accounts.get(account_id, None)
        if self.account_id is not None:
            return f"Account ID: {self.account_id}\nBalance: {self.balance}"
        else:
            return "Account not found"

    def deposit(self, account_id):
        """deposits an amount to a specific account, updating the balance."""
        if self.account_id is not None:
            # self.accounts[account_id] += amount
            amount = int(input("Input deposit amount: "))
            self.balance += amount
            return f"Deposited: {amount}\nNew Balance: {self.balance}"
        else:
            return "Account not found"

    def withdrawal(self, account_id):
        """withdraws an amount from a specific account, updating the balance if
            sufficient funds exist."""
        amount = int(input("Input withdrawal amount: "))
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrawal: {amount}\nNew Balance: {self.balance}"
        else:
            return "Insufficient funds"

    def account_summary(self, account_id):
        """prints a summary of an account, including the account ID and current
        balance."""
        if self.account_id is not None:
            return f"Account ID: {account_id}\nCurrent Balance: {self.balance}"
        else:
            return "Account not found"


if __name__ == "__main__":
    account1 = Banking(account_id=None, balance=None)
    print(account1.account_summary())



