import sys

from pydantic import BaseModel

from src import MermaidGenerator, Relations


class Animal(BaseModel):
    pass


class Fish(Animal):
    gill: str = "gill"

    def swim(self):
        pass


class Beast(Animal):
    legs: int

    def run(self):
        pass


class Bird(Animal):
    winds: int

    def fly(self):
        pass


class Dog(Beast):
    pass


class Cat(Beast):
    pass


class Salmon(Fish):
    pass


class Eagle(Bird):
    pass


if __name__ == "__main__":
    current_module = sys.modules["__main__"]
    mg = MermaidGenerator(current_module)
    chart = mg.generate_chart(relations=Relations.Inheritance)

    with open("./examples/animals.md", mode="w") as f:
        f.write(chart)
        f.close()
