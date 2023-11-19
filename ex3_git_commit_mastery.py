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

    def deposit(self, account_id):
        """deposits an amount to a specific account, updating the balance."""
        deposit = input("Choose Deposit Amount: ")
        balance = int(deposit) + self.balance
        return f"Deposited: {deposit}\nNew Balance: {balance}"

    def withdrawal(self):
        """withdraws an amount from a specific account, updating the balance if
            sufficient funds exist."""
        withdrawal = input("Choose Withdrawal Amount: ")
        if withdrawal > self.balance:
            balance = self.balance - withdrawal
        else:
            print("Insufficient funds")
        return f"Withdrawal: {withdrawal}\nNew Balance: {balance}"

    def account_summary(self):
        """prints a summary of an account, including the account ID and current
        balance."""
        return self.account_id, self.balance