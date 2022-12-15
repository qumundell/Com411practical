from inhabitant import Inhabitant


class Robot(Inhabitant):
    def __init__(self):
        super().__init__()
        self.laws = ""

    def the_laws(self):
        return self.laws

    def display(self):
        print(f"I am {self.name}")

    def __repr__(self):
        return f'robot(name={self.name}, age={self.age})'

    def __str__(self):
        return f'Robot {self.name} is {self.age} years old.'