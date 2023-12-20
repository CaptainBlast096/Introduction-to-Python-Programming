"""
Author: Jaleel Rogers

Purpose: The purpose of this project is to resemble a bank account. The alterations made to the program should add
two classes of interest for the two bank accounts.

Last edit: 10/15/21 11:25 PM

Course: Introduction to Programming Using Python - COP2034

Class Work: Assignment 7 - Bank
"""

from functools import reduce


class BankError(Exception):
    """Used for raising errors relating to the operations of the bank."""


class Bank:
    """Used for managing several savings accounts."""

    def __init__(self):
        """Constructs the initial list of accounts."""
        self.accounts = []

    def addAccount(self, account):
        """Adds a new account to the list of accounts."""
        self.accounts.append(account)

    def computeInterest(self):  # Use this for simple interest and period interest
        """Computes the interest for every account."""
        for account in self.accounts:
            account.computeInterest()

    def __str__(self):
        """Outputs the information associated with each account on a separate line."""
        accountStrings = map(lambda account: "\t" + str(account), self.accounts)
        accountsString = reduce(lambda account1, account2: account1 + "\n" + account2, accountStrings)
        return "Bank(\n" + accountsString + "\n)"

    def __init__(self):
        """Constructs the initial list of accounts."""
        self.accounts = []


class SavingsAccount:  # Can modify
    """A single account, that has a balance, a name, and a pin number."""

    # A default interest rate used for when interest is not specified.
    DEFAULT_INTEREST_RATE = .05

    def __init__(self, name, pin, balance=0.0):
        """Constructs the savings account."""
        if balance < 0:
            raise BankError()
        self.name = name
        self.pin = pin
        self.balance = balance

    # Getters
    def getName(self):
        return self.name

    def getPin(self):
        return self.pin

    def getBalance(self):
        return self.balance

    # Mutators
    def deposit(self, amount):
        if amount < 0:
            raise BankError()
        self.balance += amount

    def withdraw(self, amount):
        if self.getBalance() - amount < 0 or amount < 0:
            raise BankError()
        self.balance -= amount

    def computeInterest(self):
        """Calculates the interest and increases the balance by the interest."""
        interest = self.getBalance() * SavingsAccount.DEFAULT_INTEREST_RATE
        self.deposit(interest)

    def __str__(self):
        return f"Name: {self.getName():10} PIN: {self.getPin():6} Balance: {self.getBalance():8.2f} "

    pass
    # Use inheritance for two original classes


class SimpleInterest(SavingsAccount):
    def __init__(self, r, name, pin, balance=0.0, ):
        # Set parameters to equal themselves
        self.r = r

        if balance < 0:
            raise BankError()
        self.name = name
        self.pin = pin
        self.balance = balance

    def computeInterest(self):  # Use this for simple interest and period interest

        interest = self.getBalance() * self.r
        self.deposit(interest)


class PeriodInterest(SavingsAccount):
    def __init__(self, r, p, i, name, pin, balance=0.0, ):
        self.r = r
        self.p = p
        self.i = i


        if balance < 0:
            raise BankError()
        self.name = name
        self.pin = pin
        self.balance = balance

    # Figure out how to use if else statement with period interest
    def computeInterest(self):  # Use this for simple interest and period interest

        # If-else statement to get the period interest
        if self.i == self.p:
            self.i = 1
            interest = self.getBalance() * self.r
            self.deposit(interest)
        else:
            self.i += 1


def setupBank():  # Can only modify this function of originally code for experiment
    """Sets up the bank for the use in the demonstration of interest calculation."""
    account1 = SimpleInterest(0.01, "Account1", "1234", 100)
    account2 = PeriodInterest(0.05, 2, 1, "Account2", "2345", 1000)

    bank = Bank()
    bank.addAccount(account1)
    bank.addAccount(account2)
    return bank


def main():
    """Demonstrates the effect of interest calculation."""
    bank = setupBank()

    for i in range(6):
        print(bank)
        bank.computeInterest()


if __name__ == '__main__':
    main()
# Success
