class User:

    def __init__(self, name):
        self.name = name
        self.account = BankAccount(name, int_rate=0.1, balance=0)

    def make_deposit(self, amount):
        self.account.deposit += amount
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw -= amount
        return self

    def display_user_balance(self):
        return self.account.display_account_info


class BankAccount:

    def __init__(self, name, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        self.name = name

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
        print(f"{self.name}'s Account Balance:" + str(self.balance))
        return self


    def yield_interest(self):
        self.balance = (self.balance * self.int_rate) + self.balance
        return self

Matt = User("Matt")
Mike = User("Mike")
George = User("George")

Matt.account.deposit(500)
Mike.account.deposit(400).withdraw(500)

Matt.account.display_account_info()                       
Mike.account.display_account_info()
