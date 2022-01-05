def be_cheerful(name="Mr.Nibbles", repeat=2):
    print(f"Good morning {name}\n" * repeat)

be_cheerful("Molly")
be_cheerful()
be_cheerful(repeat=4, name="Benny Bob",)

# Other example
# set defaults when declaring the parameters
def be_cheerful(name='', repeat=2):
	print(f"good morning {name}\n" * repeat)
be_cheerful()   # output: good morning (repeated on 2 lines)
be_cheerful("tim")  # output: good morning tim (repeated on 2 lines)
be_cheerful(name="john")    # output: good morning john (repeated on 2 lines)
be_cheerful(repeat=6)   # output: good morning (repeated on 6 lines)
be_cheerful(name="michael", repeat=5)   # output: good morning michael (repeated on 5 lines)
# NOTE: argument order doesn't matter if we are explicit when sending in our arguments!
be_cheerful(repeat=3, name="kb")    # output: good morning kb (repeated on 3 lines)

"""Debugging"""

#Example
def mulitply(num_list, num):
    for x in range(len(num_list)):
        num_list[x] *= num
    return num_list
a = [2,4,10,16]
b = mulitply(a, 5)
print(b)
# output: [10,20,50,80]
