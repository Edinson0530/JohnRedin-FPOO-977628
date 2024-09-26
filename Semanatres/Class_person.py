#----------------
#person

#dni: int
#name: str
#lastname: int
#role: int
#----------------

class person:
    def __init__(self, dni: int, name: str, lastname: int, role: int,):
        self.dni = dni
        self.name = name
        self.lastname = lastname
        self.role = role

    def __repr__(self):
        return f"information={self.dni} {self.name} {self.lastname} {self.role}"

person1 = person(dni=123, name="Luisitocomunica", lastname="Velez", role=1)
person2 = person(dni=1234, name="El", lastname="Semento", role=2)
person3 = person(dni=12345, name="Mbappe", lastname="Barriga", role=3)
person4 = person(dni=123456, name="Messi", lastname="PechoFrio", role=4)

print(person1)
print(person2)
print(person3)
print(person4)