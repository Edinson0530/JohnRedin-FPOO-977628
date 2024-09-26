from faker import Faker
import random

fake = Faker()
people_list = []

def generate_people(num_people):

    people_list = []

    for i in range(num_people):
        person={
            "dni": i + 1,
            "name": fake.first_name(),
            "lastname": fake.last_name(),
            "role":random.randint(1,3)
        }
        people_list.append(person)
    return people_list


def select_role():
    
    for person in people_list:
        if(person["role"]== 1):
            person["role"] = "Administrativo"
        elif(person["role"]== 2):
            person["role"] = "Profesor"
        else:
            person["role"] = "Estudiante"

def match_role():
    for person in people_list:
        match person["role"]:
            case 1:
                person["role"] = "Administrativo"
            case 2:
                person["role"] = "Profesor"
            case 3:
                person["role"] = "Estudiante"               
        
def print_people():
        for persona in people_list:
            print(persona)


number =  int(input("por favor ingrese la cantidad de:"))
generate_people(number)
select_role()
match_role()
print_people()