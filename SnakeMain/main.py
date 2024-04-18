import pytest


# Step 1: Write Test
def test_bank_account():
    # Test deposit method with positive amount
    account = BankAccount()
    account.deposit(100)
    assert account.get_balance() == 100

    # Test deposit method with zero amount
    with pytest.raises(ValueError):
        account.deposit(0)

    # Test deposit method with negative amount
    with pytest.raises(ValueError):
        account.deposit(-50)

    # Test withdraw method
    account.withdraw(50)
    assert account.get_balance() == 50

    # Test withdraw with insufficient funds
    with pytest.raises(ValueError):
        account.withdraw(100)


# Step 3: Write Code
class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if self.balance < amount:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def get_balance(self):
        return self.balance