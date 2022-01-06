class User:
    # class attributes get defined in the class
    bank_name = "First National Dojo"
    # now our method has 2 parameters!
    def __init__(self, name, email_address):
        # we assign them accordingly
        self.name = name
        self.email = email_address
        # the account balance is set to 0
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):     # takes an argument that is the amount of the argument
        self.account_balance += amount  # the specific user's account increases by the value received
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
# print(guido.name) # output: Guido van Rossum
# print(monty.name) # output: Monty Python

guido.make_deposit(100)
guido.make_deposit(200)
monty.make_deposit(50)
print(guido.account_balance) # output: 300
print(monty.account_balance) # output: 50


# User()
# guido = User()
# monty = User()
# # Accessing the instance's attributes
# print(guido.name) # output: Michael
# print(monty.name) # output: Michael

# guido.name = "Guido"
# print(guido.name)
# monty.name = "Monty"
# print(monty.name)

# guido.bank_name = "Dojo Credit Union"
# print(guido.bank_name) # output: Dojo Credit Union
# print(monty.bank_name) # output: First National Dojo

# User.bank_name = "Bank of Dojo"
# print(guido.bank_name) # output: Bank of Dojo
# print(monty.bank_name) # output: Bank of Dojo

