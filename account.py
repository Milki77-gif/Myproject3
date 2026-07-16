class Account:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited", amount, "ETB")
        else:
            print("Deposit must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be positive.")
        elif amount > self.balance:
            print("Not enough money.")
        else:
            self.balance -= amount
            print("Withdrew", amount, "ETB")

    def statement(self):
        print("Owner:", self.owner)
        print("Account number:", self.account_number)
        print("Balance:", self.balance, "ETB")


account1 = Account("Abebe", "ADDIS001", 5000)
account1.deposit(1000)
account1.withdraw(2000)
account1.statement()

account2 = Account("Hana", "ADDIS002", 3000)
account2.deposit(-100)
account2.withdraw(4000)
account2.deposit(500)
account2.statement()
