class Inhabitant:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.energy = 100

    def grow(self):
        self.age += 1

    def eat(self, amount):
        self.energy += amount

    def move(self, distance):
        if self.energy < distance:
            print("Too tired to move that distance")
        else:
            self.energy -= distance
