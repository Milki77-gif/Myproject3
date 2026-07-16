class Account:
    """Minimal Account with encapsulated balance."""

    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = float(balance)

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def statement(self):
        return f"Owner: {self.owner} | Acc: {self.account_number} | Balance: {self.balance}"


class SavingsAccount(Account):
    """SavingsAccount overrides withdraw to enforce a minimum balance."""

    def __init__(self, owner, account_number, balance=0, minimum_balance=100):
        super().__init__(owner, account_number, balance)
        self.minimum_balance = float(minimum_balance)

    def withdraw(self, amount):
        if amount <= 0:
            return
        if self.balance - amount < self.minimum_balance:
            return
        super().withdraw(amount)


# Tiny demo for presentation (uses your name 'Milki')
if __name__ == "__main__":
    a = Account("Milki", "ACC001", 1000)
    a.deposit(100)
    a.withdraw(50)
    print(a.statement())

