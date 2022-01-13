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
        username = self.name
        balance = self.account_balance
        print(f"User: {username} , Balance: {balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        self.display_user_balance()
        other_user.display_user_balance()
        return self


guido = User("Guido van Rossum")
monty = User("Monty Python")
geralt = User("Geralt of Rivia")

guido.make_deposit(20).make_deposit(50).make_deposit(30).make_withdrawal(15).display_user_balance().transfer_money(geralt, 14)

monty.make_deposit(50).make_deposit(100).make_withdrawal(20).make_withdrawal(7).display_user_balance()

geralt.make_deposit(500).make_withdrawal(5).make_withdrawal(18).make_withdrawal(10).display_user_balance()
