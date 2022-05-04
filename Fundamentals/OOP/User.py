class User:

    def __init__(self, name):
        self.name = name
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        return self.account_balance

Matt = User("Matt")
Mike = User("Mike")
George = User("George")

Matt.make_deposit(750).make_deposit(750).make_deposit(750).make_withdrawal(500)
print(Matt.account_balance)

Mike.make_deposit(750).make_deposit(750).make_withdrawal(500).make_withdrawal(500)
print(Mike.account_balance)

George.make_deposit(1750).make_withdrawal(500).make_withdrawal(500).make_withdrawal(500)
print(George.account_balance)
