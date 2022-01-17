import Pets

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

rush = Pets.Pet("Rush", "Dog", "Fetch", 100, 200, "Barks")
megaman = Ninja("Mega", "Man", rush, "bolts", "batteries")

megaman.walk()
megaman.feed()
megaman.bathe()