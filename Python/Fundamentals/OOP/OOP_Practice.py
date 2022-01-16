from multiprocessing import parent_process


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

"""
4 Pillars of OOP
"""

# 1. Encapsulation - Group code together into objects, hence Object Oriented Programming; Use classes or "coding blueprints" 
# to define what our objects are and how they behave. Encapsulate attributes and methods in our class

class CoffeM:
    def __init__(self, name):
        self.name = name
        self.water_temp = 200
    def brew_now(self, beans):
        print(f"Using {beans}!")
        print("Brew now brown cow!")
    def clean(self):
        print("Cleaning!")

# 2. Inheritance - Pass along attributes and methods from one class into a "sub-class" or child class and not have to re-write the code.
# Child classes can be more specific; using "super" will call methods

class CappucinoM(CoffeM):
    def __init__(self, name):
        super().__init__(name)
        self.milk = "whole"
    def make_cappuccino(self, beans):
        super.brew_now(beans)
        print("Frothy!!!")
# 3. Polymorphism - "Many forms" and the idea that a child class can have a different version of a method than the parent class
# This example, child class has a clean method and so does parent. Depending on class, clean method will do different things
    def clean(self):
        print("Cleaning the froth!")

# 4. Abstraction - Extension of Encapsulation and we can hide attributes or methods that a Barista doesn't need to know about, like CoffeeM.
# The way the Barista can make a cup of coffee in a simpler manner

class Barista:
    def __init__(self, name):
        self.name = name
        self.cafe = CoffeM("Cafe")
    def make_coffee(self):
        self.cafe.brew_now()


"""
Overriding & Polymorphism
"""

# Override parent function in child class

class Parent:
    def method_a(self):
        print("invoking PARENT method_a!")
class Child(Parent):
    def method_a(self):
        print("invoking CHILD method_a!")
dad = Parent()
son = Child()
dad.method_a()
son.method_a()  # notice this overrides the Parent method

# Polymorphism allows us to specify common methods in an  "abstract" level and implement them in particular instances
# the process of using an operator or function in defferent ways for different data input

# we'll use the Person class to demonstrate polymorphism
# in which multiple classes inherit from the same class but behave in different ways

class Person:
    def pay_bill(self):
        raise NotImplementedError
# Millionaire inherits from Person
class Millionaire(Person):
    def pay_bill(self):
        print("Here you go! Keep the change!")
# Grad Student also inherits from the Person class
class GradStudent(Person):
    def pay_bill(self):
        print("Can I owe you ten bucks or do the dishes?")