from abc import ABC

# Esta clase es abtracta
# Es no intanciable person = Person(...)

class Person(ABC):
    def __init__(self, name, lastname, age, address):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.address = address