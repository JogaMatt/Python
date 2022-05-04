import Pets

class Ninja:

    def __init__(self, first_name, last_name, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = Pet(name = "Boo", type = "cat", tricks = "lay down", health = 100, energy = 100)
        self.treats = treats
        self.pet_food = pet_food

    def feed(self):
        self.pet.eat()
        return self

    def walk(self):
        self.pet.play()
        return self

    def bathe(self):
        self.pet.noise()