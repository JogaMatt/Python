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
        return self

class Pet:

    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25
        if self.energy < 150:
            print(f"{self.name} slept and regained some energy! His energy level is now at {self.energy}")
        else:
            self.energy = 150
            print(f"Because he slept so much, {self.name}'s energy is maxed out! His energy level is now at {self.energy}" )
        return self


    def eat(self):
        self.energy += 5
        if self.energy < 150:
            print(f"{self.name} ate and regained some energy! His energy level is now at {self.energy}")
        else:
            self.energy = 150
            print(f"Because he ate so much, {self.name}'s energy is maxed out! His energy level is now at {self.energy}")
        self.health += 10
        if self.health < 150:
            print(f"{self.name} ate and regained some health! His health level is now at {self.health}")
        else:
            self.health = 150
            print(f"Because he ate so much, {self.name}'s health is maxed out! His health level is now at {self.health}")
        return self


    def play(self):
        self.health += 10
        if self.health < 150:
            print(f"{self.name} played and regained some health! His health level is now at {self.health}")
        else:
            self.health = 150
            print(f"Because he played so much, {self.name}'s health is maxed out! His health level is now at {self.health}")
        return self

    def noise(self):
        print(f"{self.name} loved his bath and made a great, big meow!")
        print(f"Here are his current levels. Health: {self.health} Energy: {self.energy}")
        return self

Sub_Zero = Ninja("Kuai", "Liang", "cat nip", "kibble")

Sub_Zero.feed().walk().bathe()