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
"""
From the 'git' point of view you did a good job however there a few things that need to be pointed out.
Please make corrections base on the following observation and submit again:

- If we want to create multiples accounts. How you keep track of them? How you make sure that the ids are unique? 
How will you recover/call the data/functions of an account that you created many instructions/days ago 
(this is regarding the data structure you are using to model the bank system)?

- what is the use of 'account_creation' if you never call it? You are using the '__init__' fro the account creating.
- Base on the defined functionality the name of the class is not correct.

Notes:
- make sure to do the needed changes, commit them as you did before and submit the changes in code and git (as before).
- make sure to define test functions per functionality/test case to test.

"""

import random

ACCOUNTS = 1


class Banking:
    def __init__(self):
        self.account_id = ACCOUNTS + 1
        self.balance = 0

    def account_creation(self):
        """creates a new account with a unique account ID and initial balance."""
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

    def account_summary(self):
        """prints a summary of an account, including the account ID and current
        balance."""
        return f"Account ID: {self.account_id}\nCurrent Balance: {self.balance}"


if __name__ == "__main__":
    user1 = Banking()
    assert user1.account_id == 2
    assert user1.balance == 0
    print(user1.account_summary())

    # print(user1.balance_inquiry())
    # assert user1.deposit(amount=5) == "Deposited: 5\nNew Balance: 15"
    # assert user1.withdrawal(amount=25) == "Insufficient funds"
    # assert user1.withdrawal(amount=5) == "Withdrawal: 5\nNew Balance: 10"

    # print(isinstance(user1, Banking))
