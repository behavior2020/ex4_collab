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
    def __init__(self):
        self.accounts = {}

    def account_creation(self):
        """creates a new account with a unique account ID and initial balance."""
        account_id = random.randint(10000000, 99999999)
        self.accounts[account_id] = 0
        return f"Account ID: {account_id}\nBalance: 0"

    def balance_inquiry(self, account_id):
        """checks the current balance of a given account ID."""
        balance = self.accounts.get(account_id, None)
        if balance is not None:
            return f"Account ID: {account_id}\nBalance: {balance}"
        else:
            return "Account not found"

    def deposit(self, account_id, amount):
        """deposits an amount to a specific account, updating the balance."""
        if account_id in self.accounts:
            self.accounts[account_id] += amount
            return f"Deposited: {amount}\nNew Balance: {self.accounts[account_id]}"
        else:
            return "Account not found"

    def withdrawal(self, account_id, amount):
        """withdraws an amount from a specific account, updating the balance if
            sufficient funds exist."""
        if account_id in self.accounts:
            self.accounts[account_id] -= amount
            return f"Withdrawal: {amount}\nNew Balance: {self.accounts[account_id]}"
        else:
            return "Insufficient funds"

    def account_summary(self, account_id):
        """prints a summary of an account, including the account ID and current
        balance."""
        if account_id in self.accounts:
            return f"Account ID: {account_id}\nCurrent Balance: {self.accounts[account_id]}"
        else:
            return "Account not found"


bank = Banking()
print(bank.account_creation())
