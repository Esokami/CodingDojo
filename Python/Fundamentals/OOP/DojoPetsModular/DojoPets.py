class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        print(f"Feeding {self.pet_food}!")
        self.pet.eat()
        return self

    def bathe(self):
        print(f"Bath time!")
        self.pet.noise()
        return self

class Pet:
    def __init__(self, name, type, tricks, health, energy, pet_noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        self.pet_noise = pet_noise

    def sleep(self):
        self.energy += 25
        print(f"Energy increased by: {self.energy}!")
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"Energy increased by: {self.energy}!")
        print(f"Health increased by: {self.health}!")
        return self

    def play(self):
        self.health += 5
        (f"Health increased by: {self.health}!")
        return self

    def noise(self):
        print(f"{self.name} {self.pet_noise}")
        return self

rush = Pet("Rush", "Dog", "Fetch", 100, 200, "Barks")
megaman = Ninja("Mega", "Man", rush, "bolts", "batteries")

megaman.walk()
megaman.feed()
megaman.bathe()