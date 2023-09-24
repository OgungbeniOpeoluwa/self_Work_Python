class MyAccount:
    def __init__(self):
        self._balance = 0

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdrawal(self, amount):
        if amount <= self._balance:
            self._balance -= amount

