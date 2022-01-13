class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        username = self.name
        balance = self.account_balance
        print(f"User: {username} , Balance: {balance}")

    def transfer_money(self, other_user, amount):
        owner = self.name
        receiver = other_user
        

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Pythong", "monty@python.com")
geralt = User("Geralt of Rivia", "whitewolf@python.com")

guido.make_deposit(20)
guido.make_deposit(50)
guido.make_deposit(30)
guido.make_withdrawal(15)
guido.display_user_balance()

monty.make_deposit(50)
monty.make_deposit(100)
monty.make_withdrawal(20)
monty.make_withdrawal(7)
monty.display_user_balance()

geralt.make_deposit(500)
geralt.make_withdrawal(5)
geralt.make_withdrawal(18)
geralt.make_withdrawal(10)
geralt.display_user_balance()