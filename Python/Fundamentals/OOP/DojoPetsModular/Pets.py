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

class Cat(Pet):
    def __init__(self, name, type, tricks, health, energy, pet_noise):
        super().__init__(name, type, tricks, health, energy, pet_noise)
    def noise(self):
        return super().noise()

yato = Cat("Yato","Cat", "Sneak", 200, 50, "Meows")
yato.noise()