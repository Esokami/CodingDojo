# Indentation practice
x = 10
if x > 50:
    print("bigger than 50")
else:
    print('smaller than 50')

# Pass example
my_string = "My String"

class EmptyClass:
    pass

for val in my_string:
    pass

"""
Primitive Data Types : Basics, most languages have these in common
"""

# Booleans : Assesses the truth value, Note uppercase T and F
is_hungry = True
has_freckles = False

# Numbers : Integers (whole numbers), Floats (decimals and complex numbers)
age = 35 # storing an int
weight = 160.57 # storing a float

# Strings : Literal text
name = "Joe Blue"

"""
Composite Types : Collections composed of the above primitive types
"""

# Tuples : Type of data that is immutable (cannot be modified after creation) and can hold a group of values. Can contain mixed data types
dog = ('Bruce', 'cocker spaniel', 19, False)
print(dog[0])   #output: Bruce
#dog[1] = 'dachsund' # Error

# Lists : Type of data that is mutable and can hold a group of values. Usually meant to store a collection of related data
empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2])    # output : Oliver
ninjas[0] = 'Francis'
ninjas.append('Micahel')
print(ninjas)           # output: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)           # output: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)           # output: ['Francis', 'Oliver']

#Dictionaries : Group of key-value pairs. Indexed by unique keys which are used to access values. 
empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack'	# updates if the key exists, adds a key-value pair if it doesn't
new_person['hobbies'] = ['climbing', 'coding']
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
w = new_person.pop('weight')	# removes the specified key and returns the value
print(w)		# output: 160.2
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}        

"""
Common Functions 
"""

# Type : Used to find value or variable's data type if user is unsure
print(type(2.63))		# output: <class 'float'>
print(type(new_person))		# output: <class 'dict'>

# Len : Used to get length of data type
print(len(new_person))		# output: 4 (the number of key-value pairs)
print(len('Coding Dojo'))	# output: 11

"""
Numbers : Int, Float, Complex
"""

# Type
print(type(24))
print(type(3.9))
print(type(3j))

# Conversion
int_to_float = float(35)
float_to_int = int(44.2)
int_to_complex = complex(35)
print(int_to_float)
print(float_to_int)
print(int_to_complex)
print(type(int_to_float))
print(type(float_to_int))
print(type(int_to_complex))

# Random
import random
print(random.randint(2,5)) # provides a random number between 2 and 5


"""
Strings 
"""

# String Literals : Any sequence of characters enclosed in single or double quotes

print("this is a sample string")

#Concatenating Strings and Variables

name = "Zen"
print("My name is", name)

name = "Zen"
print("My name is " + name)

# Type Casting or Explicit Type Conversion

#print("Hello" + 42)			# output: TypeError
print("Hello" + str(42))		# output: Hello 42

total = 35
user_val = "26"
#total = total + user_val		# output: TypeError
total = total + int(user_val)		# total will be 61

# String Interpolation : Injecting variables into strings

# F-Strings

first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.")

#String.Format()

first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# output: My name is Zen Coder and I am 27 years old.
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# output: My name is 27 Zen and I am Coder years old.

# % -Formatting : Older; Rather than curly braces, %s for string and %d for number. After string % separates the string

hw = "Hello %s" % "world" 	# with literal values
py = "I love Python %d" % 3 
print(hw, py)
# output: Hello world I love Python 3
name = "Zen"
age = 27
print("My name is %s and I'm %d" % (name, age))		# or with variables
# output: My name is Zen and I'm 27

# Built-In String Methods

x = "hello world"
print(x.title())
# output:
"Hello World"

"""
List : Similar to arrays in JS. Can be of various data types
"""
# Example 1

ninjas = ['Rozen', 'KB', 'Oliver']
my_list = ['4', ['list', 'in', 'a', 'list'], 987]
empty_list = []

# Example 2

fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)
salad = 3 * vegetables
print(salad)

# Accessing Values

drawer = ['documents', 'envelopes', 'pens']
#access the drawer with index of 0 and print value
print(drawer[0])  #prints documents
#access the drawer with index of 1 and print value
print(drawer[1]) #prints envelopes
#access the drawer with index of 2 and print value
print(drawer[2]) #prints pens

# Manipulating Lists - <list>.append(<new_element>)

x = [1,2,3,4,5]
x.append(99)
print(x)
#the output would be [1,2,3,4,5,99]

# Example below is like a slice function in JS. Python uses [] characters to return a copy of the list, constrained to the specified indices

x = [99,4,2,5,-3]
print(x[:])
#the output would be [99,4,2,5,-3]
print(x[1:])
#the output would be [4,2,5,-3];
print(x[:4])
#the output would be [99,4,2,5]
print(x[2:4])
#the output would be [2,5];

# List Built-In Functions

# len(sequence) : Returns the number of items in a sequence

my_list = [1, 'Zen', 'hi']
print(len(my_list))
# output
3

"""
Other sequences:
enumerate(sequence) : Used in a for loop context to return two-item-tuple for each item in the list, indicating the index followed 
by the value at that index

map(function, sequence) : Applies the functionto every item in the sequence you pass in. Returns a list of the results.

min(sequence) : Returns the lowest value in a sequence.

sorted(sequence) : Returns a sorted sequence.
"""

# List Built-In Methods

#list.append(value) : Specific to lists versus other sets, much like string methods

my_list = [1,5,2,8,4]
my_list.append(7)
print(my_list)
# output:
# [1,5,2,8,4,7]


"""
Tuples : Immutable; Use Parentheses instead of square brackets
"""

# Example

tuple_data = ('physics', 'chemistry', 1997, 2000)
tuple_num = (1, 2, 3, 4, 5 )
tuple_letters = "a", "b", "c", "d"

dog = ("Canis Familiaris", "dog", "carnivore", 12)
print(dog[2])
#result is: carnivore

#dog[0] = "X"
#TypeError: 'tuple' object does not support item assignment

dog = dog + ("domestic",)
#result is...
#("Canis Familiaris", "Dog", "carnivore", 12, "domestic")

dog = dog[:3] + ("man's best friend",) + dog[4:]
#result is...
#("Canis Familiaris", "Dog", "carnivore", "man's best friend", "domestic")

# Built-In Tuple Functions

#len(sequence) : Returns the length of the given tuple

x = (1,5,6,9,2)
print(len(x))
# output:
# 5

# Tuples as Return Functions

#def get_circle_area(r):
    #Return (circumference, area) of a circle of radius r
    #c = 2 * math.pi * r
    #a = math.pi * r * r
    #return (c, a)

#import language
#print(language.translate(dog))
# output would look something like: ("dog", "chien", "perro")


"""
Dictionaries | Each Key in a dictionary must be unique
"""

# Example
weekend = {"Sun": "Sunday", "Sat": "Saturday"} #literal notation
capitals = {} #create an empty dictionary then add values
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"

print(weekend["Sun"])
print(capitals["svk"])

# Removing values

value_removed = capitals.pop('svk') # will remove the key 'svk' and return it's value
del capitals['dnk'] # will delete the key, and not return anything

# Nested Dictionaries

#context = {
#    'questions': [
#        { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
#        { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
#        { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
#        { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
#    ]
#}

"""
Conditionals
"""

# Examples

#    x = 12
#    if x > 50:
#        print("bigger than 50")
#    else:
#        print("smaller than 50")
    # because x is not greater than 50, the second print statement is the only one that will execute
#    
#    x = 55
#    if x > 10:
#        print("bigger than 10")
#    elif x > 50:
#        print("bigger than 50")
#    else:
#        print("smaller than 10")
    # even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'
    
#    if x < 10:
#        print("smaller than 10")
#    # nothing happens, because the statement is false   

"""Functions"""

# Example 1
def add(a,b):   # function name: "add", parameters: a and b
    x = a + b   # process
    return x    # return value: x

# Actually calling the function
new_val = add(3, 5) # calling the add function, with arguments 3 and 5
print(new_val)      # the result of the add function gets sent back to and saved to new_val, so we will see 8

# Example 2
def say_hi(name):
    print("Hi, " + name)

# Invoking the function 3 times, passing in one argument each time
say_hi("Michael")
# Indentation practice
x = 10
if x > 50:
    print("bigger than 50")
else:
    print('smaller than 50')

# Pass example
my_string = "My String"

class EmptyClass:
    pass

for val in my_string:
    pass

"""
Primitive Data Types : Basics, most languages have these in common
"""

# Booleans : Assesses the truth value, Note uppercase T and F
is_hungry = True
has_freckles = False

# Numbers : Integers (whole numbers), Floats (decimals and complex numbers)
age = 35 # storing an int
weight = 160.57 # storing a float

# Strings : Literal text
name = "Joe Blue"

"""
Composite Types : Collections composed of the above primitive types
"""

# Tuples : Type of data that is immutable (cannot be modified after creation) and can hold a group of values. Can contain mixed data types
dog = ('Bruce', 'cocker spaniel', 19, False)
print(dog[0])   #output: Bruce
#dog[1] = 'dachsund' # Error

# Lists : Type of data that is mutable and can hold a group of values. Usually meant to store a collection of related data
empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2])    # output : Oliver
ninjas[0] = 'Francis'
ninjas.append('Micahel')
print(ninjas)           # output: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)           # output: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)           # output: ['Francis', 'Oliver']

#Dictionaries : Group of key-value pairs. Indexed by unique keys which are used to access values. 
empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack'	# updates if the key exists, adds a key-value pair if it doesn't
new_person['hobbies'] = ['climbing', 'coding']
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
w = new_person.pop('weight')	# removes the specified key and returns the value
print(w)		# output: 160.2
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}        

"""
Common Functions 
"""

# Type : Used to find value or variable's data type if user is unsure
print(type(2.63))		# output: <class 'float'>
print(type(new_person))		# output: <class 'dict'>

# Len : Used to get length of data type
print(len(new_person))		# output: 4 (the number of key-value pairs)
print(len('Coding Dojo'))	# output: 11

"""
Numbers : Int, Float, Complex
"""

# Type
print(type(24))
print(type(3.9))
print(type(3j))

# Conversion
int_to_float = float(35)
float_to_int = int(44.2)
int_to_complex = complex(35)
print(int_to_float)
print(float_to_int)
print(int_to_complex)
print(type(int_to_float))
print(type(float_to_int))
print(type(int_to_complex))

# Random
import random
print(random.randint(2,5)) # provides a random number between 2 and 5


"""
Strings 
"""

# String Literals : Any sequence of characters enclosed in single or double quotes

print("this is a sample string")

#Concatenating Strings and Variables

name = "Zen"
print("My name is", name)

name = "Zen"
print("My name is " + name)

# Type Casting or Explicit Type Conversion

#print("Hello" + 42)			# output: TypeError
print("Hello" + str(42))		# output: Hello 42

total = 35
user_val = "26"
#total = total + user_val		# output: TypeError
total = total + int(user_val)		# total will be 61

# String Interpolation : Injecting variables into strings

# F-Strings

first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.")

#String.Format()

first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
# output: My name is Zen Coder and I am 27 years old.
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))
# output: My name is 27 Zen and I am Coder years old.

# % -Formatting : Older; Rather than curly braces, %s for string and %d for number. After string % separates the string

hw = "Hello %s" % "world" 	# with literal values
py = "I love Python %d" % 3 
print(hw, py)
# output: Hello world I love Python 3
name = "Zen"
age = 27
print("My name is %s and I'm %d" % (name, age))		# or with variables
# output: My name is Zen and I'm 27

# Built-In String Methods

x = "hello world"
print(x.title())
# output:
"Hello World"

"""
List : Similar to arrays in JS. Can be of various data types
"""
# Example 1

ninjas = ['Rozen', 'KB', 'Oliver']
my_list = ['4', ['list', 'in', 'a', 'list'], 987]
empty_list = []

# Example 2

fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)
salad = 3 * vegetables
print(salad)

# Accessing Values

drawer = ['documents', 'envelopes', 'pens']
#access the drawer with index of 0 and print value
print(drawer[0])  #prints documents
#access the drawer with index of 1 and print value
print(drawer[1]) #prints envelopes
#access the drawer with index of 2 and print value
print(drawer[2]) #prints pens

# Manipulating Lists - <list>.append(<new_element>)

x = [1,2,3,4,5]
x.append(99)
print(x)
#the output would be [1,2,3,4,5,99]

# Example below is like a slice function in JS. Python uses [] characters to return a copy of the list, constrained to the specified indices

x = [99,4,2,5,-3]
print(x[:])
#the output would be [99,4,2,5,-3]
print(x[1:])
#the output would be [4,2,5,-3];
print(x[:4])
#the output would be [99,4,2,5]
print(x[2:4])
#the output would be [2,5];

# List Built-In Functions

# len(sequence) : Returns the number of items in a sequence

my_list = [1, 'Zen', 'hi']
print(len(my_list))
# output
3

"""
Other sequences:
enumerate(sequence) : Used in a for loop context to return two-item-tuple for each item in the list, indicating the index followed 
by the value at that index

map(function, sequence) : Applies the functionto every item in the sequence you pass in. Returns a list of the results.

min(sequence) : Returns the lowest value in a sequence.

sorted(sequence) : Returns a sorted sequence.
"""

# List Built-In Methods

#list.append(value) : Specific to lists versus other sets, much like string methods

my_list = [1,5,2,8,4]
my_list.append(7)
print(my_list)
# output:
# [1,5,2,8,4,7]


"""
Tuples : Immutable; Use Parentheses instead of square brackets
"""

# Example

tuple_data = ('physics', 'chemistry', 1997, 2000)
tuple_num = (1, 2, 3, 4, 5 )
tuple_letters = "a", "b", "c", "d"

dog = ("Canis Familiaris", "dog", "carnivore", 12)
print(dog[2])
#result is: carnivore

#dog[0] = "X"
#TypeError: 'tuple' object does not support item assignment

dog = dog + ("domestic",)
#result is...
#("Canis Familiaris", "Dog", "carnivore", 12, "domestic")

dog = dog[:3] + ("man's best friend",) + dog[4:]
#result is...
#("Canis Familiaris", "Dog", "carnivore", "man's best friend", "domestic")

# Built-In Tuple Functions

#len(sequence) : Returns the length of the given tuple

x = (1,5,6,9,2)
print(len(x))
# output:
# 5

# Tuples as Return Functions

#def get_circle_area(r):
    #Return (circumference, area) of a circle of radius r
    #c = 2 * math.pi * r
    #a = math.pi * r * r
    #return (c, a)

#import language
#print(language.translate(dog))
# output would look something like: ("dog", "chien", "perro")


"""
Dictionaries | Each Key in a dictionary must be unique
"""

# Example
weekend = {"Sun": "Sunday", "Sat": "Saturday"} #literal notation
capitals = {} #create an empty dictionary then add values
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"

print(weekend["Sun"])
print(capitals["svk"])

# Removing values

value_removed = capitals.pop('svk') # will remove the key 'svk' and return it's value
del capitals['dnk'] # will delete the key, and not return anything

# Nested Dictionaries

#context = {
#    'questions': [
#        { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
#        { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
#        { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
#        { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
#    ]
#}

"""
Conditionals
"""

# Examples

#    x = 12
#    if x > 50:
#        print("bigger than 50")
#    else:
#        print("smaller than 50")
    # because x is not greater than 50, the second print statement is the only one that will execute
#    
#    x = 55
#    if x > 10:
#        print("bigger than 10")
#    elif x > 50:
#        print("bigger than 50")
#    else:
#        print("smaller than 10")
    # even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'
    
#    if x < 10:
#        print("smaller than 10")
#    # nothing happens, because the statement is false   

"""Functions"""

# Example 1
def add(a,b):   # function name: "add", parameters: a and b
    x = a + b   # process
    return x    # return value: x

# Actually calling the function
new_val = add(3, 5) # calling the add function, with arguments 3 and 5
print(new_val)      # the result of the add function gets sent back to and saved to new_val, so we will see 8

# Example 2
def say_hi(name):
    print("Hi, " + name)

# Invoking the function 3 times, passing in one argument each time
say_hi("Michael")
say_hi("Anna")
say_hi("Eli")

# Example 3
def say_hello(name):
    return "Hello " + name
greeting = say_hello("Michael")
print(greeting)

# Example 4
def add2(a, b):
    x = a + b
    return x
sum1 = add2(4,6)
sum2 = add2(1,4)
sum3 = sum1 + sum2
print(sum3)


