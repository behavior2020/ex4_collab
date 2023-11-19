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
        self.account_id = account_id
        self.balance = balance

    def account_creation(self):
        """creates a new account with a unique account ID and initial balance."""
        self.account_id = random.randint(10000000, 99999999)
        self.balance = 0
        return f"Account ID: {self.account_id}\nBalance: {self.balance}"

    def balance_inquiry(self):
        """checks the current balance of a given account ID."""
        return f"Account ID: {self.account_id}\nBalance: {self.balance}"

    def deposit(self, amount):
        """deposits an amount to a specific account, updating the balance."""
        self.balance += amount
        return f"Deposited: {amount}\nNew Balance: {self.balance}"

    def withdrawal(self, amount):
        """withdraws an amount from a specific account, updating the balance if
            sufficient funds exist."""
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrawal: {amount}\nNew Balance: {self.balance}"
        else:
            return "Insufficient funds"

    def account_summary(self, account_id, balance):
        """prints a summary of an account, including the account ID and current
        balance."""
        return f"Account ID: {self.account_id}\nCurrent Balance: {self.balance}"


if __name__ == "__main__":
    user1 = Banking(account_id=12345678, balance=10)
    assert user1.account_id == 12345678
    assert user1.balance == 10

    print(user1.balance_inquiry())
    assert user1.deposit(amount=5) == "Deposited: 5\nNew Balance: 15"
    assert user1.withdrawal(amount=25) == "Insufficient funds"
    assert user1.withdrawal(amount=5) == "Withdrawal: 5\nNew Balance: 10"
