class BankAccount:
    accounts = []
    int_rate = 0.04
    balance = 0
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
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if (self.balance > 0):
            self.balance += self.balance * self.int_rate
        return self

    @classmethod
    def all_accounts(cls):
        #print(f"{cls.accounts} accounts activated")
        #display all accounts info
        for account in cls.accounts:
            account.display_account_info()

ciri = BankAccount(0.03, 0)
geralt = BankAccount(0.05, 1000)
yennefer = BankAccount(0.02, 5)

ciri.deposit(300).deposit(100).deposit(45).withdraw(20).yield_interest().display_account_info()
geralt.deposit(250).deposit(189).withdraw(45).withdraw(225).withdraw(62).withdraw(29).yield_interest().display_account_info()
yennefer.withdraw(20).yield_interest().display_account_info()

BankAccount.all_accounts()