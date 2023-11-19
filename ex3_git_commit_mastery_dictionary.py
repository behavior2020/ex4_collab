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
    all_accounts = {}

    def __init__(self, account_id, balance=0):
        # accounts = {}
        self.account_id = account_id
        self.balance = balance

    def account_creation(self):
        """creates a new account with a unique account ID and initial balance."""
        self.account_id = random.randint(10000000, 99999999)
        # self.accounts[account_id] = 0
        self.balance = 0
        Banking.all_accounts[self.account_id] = self.balance
        return f"Account ID: {self.account_id}\nBalance: {self.balance}"

    def balance_inquiry(self, account_id):
        """checks the current balance of a given account ID."""
        # balance = self.accounts.get(account_id, None)
        if account_id in Banking.all_accounts:
            return f"Account ID: {self.account_id}\nBalance: {Banking.all_accounts[account_id]}"
        else:
            return "Account not found"

    def deposit(self, account_id, amount):
        """deposits an amount to a specific account, updating the balance."""
        Banking.all_accounts[account_id] += amount
        return f"Deposited: {amount}\nNew Balance: {Banking.all_accounts[account_id]}"

    def withdrawal(self, account_id, amount):
        """withdraws an amount from a specific account, updating the balance if
            sufficient funds exist."""
        if amount <= Banking.all_accounts[account_id]:
            Banking.all_accounts[account_id] -= amount
            return f"Withdrawal: {amount}\nNew Balance: {Banking.all_accounts[account_id]}"
        else:
            return "Insufficient funds"

    def account_summary(self, account_id):
        """prints a summary of an account, including the account ID and current
        balance."""
        if account_id in Banking.all_accounts:
            return f"Account ID: {self.account_id}\nCurrent Balance: {Banking.all_accounts[account_id]}"
        else:
            return "Account not found"


if __name__ == "__main__":
    banking_instance = Banking(account_id=None)
    new_customer = banking_instance.account_creation()
    print(new_customer)

    balance_inquiry = banking_instance.balance_inquiry(account_id=None)
    print(new_customer)

    deposit_test = banking.deposit(account_id=None, amount=20)
    print(deposit_test)