class Account:
    """A basic bank account with encapsulated balance.

    Balance is private; subclasses may use the protected `_change_balance` helper.
    """

    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = float(balance)

    @property
    def balance(self):
        return self.__balance

    def _change_balance(self, amount):
        """Protected helper to change the private balance value."""
        self.__balance += amount

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be positive.")
            return False
        self._change_balance(amount)
        print(f"Deposited {amount} ETB")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be positive.")
            return False
        if amount > self.balance:
            print("Not enough money.")
            return False
        self._change_balance(-amount)
        print(f"Withdrew {amount} ETB")
        return True

    def statement(self):
        print("Owner:", self.owner)
        print("Account number:", self.account_number)
        print(f"Balance: {self.balance} ETB")


class SavingsAccount(Account):
    """Savings account that enforces a minimum balance and supports interest.

    Demonstrates inheritance and method overriding: `withdraw` is overridden
    to enforce `minimum_balance`. It also adds `add_interest`.
    """

    def __init__(self, owner, account_number, balance=0, minimum_balance=100, interest_rate=0.02):
        super().__init__(owner, account_number, balance)
        self.minimum_balance = float(minimum_balance)
        self.interest_rate = float(interest_rate)

    def withdraw(self, amount):
        # Override: prevent withdrawing below minimum balance
        if amount <= 0:
            print("Withdrawal must be positive.")
            return False
        if self.balance - amount < self.minimum_balance:
            print(f"Cannot withdraw: minimum balance of {self.minimum_balance} ETB must remain")
            return False
        # reuse base class logic for actual withdrawal
        return super().withdraw(amount)

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self._change_balance(interest)
        print(f"Added interest: {interest:.2f} ETB (rate={self.interest_rate})")

    def statement(self):
        print("Savings Account")
        super().statement()


def _demo():
    print("--- Demo: Account ---")
    account1 = Account("Abebe", "ADDIS001", 5000)
    account1.deposit(1000)
    account1.withdraw(2000)
    account1.statement()

    print("\n--- Demo: SavingsAccount (overriding withdraw & interest) ---")
    savings1 = SavingsAccount("Selam", "SAVE001", 1000, minimum_balance=200, interest_rate=0.05)
    savings1.withdraw(950)   # should fail due to minimum_balance
    savings1.withdraw(700)   # should succeed
    savings1.add_interest()
    savings1.statement()


if __name__ == "__main__":
    _demo()

