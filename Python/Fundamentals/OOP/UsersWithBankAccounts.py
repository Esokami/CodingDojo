class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {
            "checkings" : BankAccount(0.02, 0),
            "savings" : BankAccount(0.05, 0)
        }

    def display_user_balance(self):
        checking = self.account["checkings"].display_account_info()
        savings = self.account["savings"].display_account_info()
        print(f"User: {self.name} , Checkings Balance: {checking}")
        print(f"User: {self.name} , Savings Balance: {savings}")
        return self

    def transfer_money(self, other_user, amount):
        self.account -= amount
        other_user.account += amount
        self.display_user_balance()
        other_user.display_user_balance()
        return self

class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        return f"{self.balance}"

    def yield_interest(self):
        if (self.balance > 0):
            self.balance += self.balance * self.int_rate
        return self

geralt = User("Geralt of Rivia", "whitewolf@python.com")
geralt.account["checkings"].deposit(1000).withdraw(35)
geralt.account["savings"].deposit(5000).yield_interest()
geralt.display_user_balance()
