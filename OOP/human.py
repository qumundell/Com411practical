from inhabitant import Inhabitant


class Human(Inhabitant):
    def __init__(self):
        super().__init__()
        self.clothing = []

    def dress(self, clothing):
        self.clothing.append(clothing)

    def undress(self, clothing):
        self.clothing.remove(clothing)

    def __repr__(self):
        return f'human(name={self.name}, age={self.age})'

    def __str__(self):
        return f'Human {self.name} is {self.age} years old.'

