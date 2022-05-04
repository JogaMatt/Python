class BankAccount:

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self


    def display_account_info(self):
        print("Balance:" + str(self.balance))


    def yield_interest(self):
        self.balance = (self.balance * self.int_rate) + self.balance
        return self

Matt = BankAccount(0.1, 0)
Mike = BankAccount(0.3, 900)


Matt.deposit(500).deposit(500).deposit(500).yield_interest().withdraw(1600).display_account_info()
Mike.deposit(500).deposit(500).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()


print(Matt.balance)
print(Mike.balance)
