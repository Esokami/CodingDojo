"""
1. Update Values in Dictionaries and Lists
"""
x = [[5,2,3], [10,8,9]]
students = [
    {"first_name": "Michael", "last_name": "Jordan"},
    {"first_name": "John", "last_name": "Rosales"}
]
sports_directory = {
    "basketball" : ["Kobe", "Jordan", "James", "Curry"],
    "soccer" : ["Messi", "Ronaldo", "Rooney"]
}
z = [{"x": 10, "y": 20}]

x[1][0] = 15
print(x)

students[0]["last_name"] = "Bryant"
print(students)

sports_directory["soccer"][0] = "Andres"
print(sports_directory)

z[0]["y"] =30
print(z) 

"""
2. Iterate Through a List of Dictionaries
"""
students = [
                {"first_name": "Michael", "last_name": "Jordan"},
                {"first_name": "John", "last_name": "Rosales"},
                {"first_name": "Mark", "last_name": "Guillen"},
                {"first_name": "KB", "last_name": "Tonel"},
        ]

def iterateDictionary(students):
    for i in range(len(students)):
        new = ""
        for key, value in students[i].items():
            new += f" {key} - {value},"
        print(new)
iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

"""
3. Get Values From a List of Dictionaries
"""
def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        for key, value in some_list[i].items():
            if (key == key_name):
                print(value)
iterateDictionary2("first_name", students)
iterateDictionary2("last_name", students)

"""
4. Iterate Through a Dictionary with List Values
"""
dojo = {
    "locations": ["San Jose", "Seattle", "Dallas", "Chicago", "Tulsa", "DC", "Burbank"],
    "instructors": ["Michael", "Amy", "Eduardo", "Josh", "Graham", "Patrick", "Minh", "Devon"]
}

def printInfo(some_dict):
    for key, value in some_dict.items():
        print(f"{len(value)} {key}")
        for i in range(len(value)):
            print(value[i])

printInfo(dojo)
