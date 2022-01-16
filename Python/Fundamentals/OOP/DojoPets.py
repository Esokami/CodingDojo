class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = super.__init__(Pet)
        self.treats = treats
        self.pet_food = pet_food
    
    def walk(self):
        super.play(self.pet)
        print(f"Walking {self.pet}!")
    
    def feed():
        pass

    def bathe():
        pass

class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        if (self.type == "Cat"):
            print("Meow!")
        elif (self.type == "Dog"):
            print("Woof!")
        return self

zero = Ninja("Megaman", "Zero", "Rush", "Bolts", "Batteries")
rush = Pet("Rush", "Dog", "Fetch", 100, 200)

zero.walk()