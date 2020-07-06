#python 3.5.2
class Person:
    def __init__(self):
        print("Person class is created")
    def __del__(self):
        print("Person class object is destroyed")
    def setFirstName(self,firstName):
        self.firstName=firstName
    def setLastName(self,lastName):
        self.lastName=lastName
    def printFullName(self):
        print(self.firstName," ",self.lastName)

class MalePerson(Person):
    pass
class FemalePerson(Person):
    pass   

maleperson=MalePerson()
maleperson.setFirstName("Prasad")
maleperson.setLastName("Lakkakula")
maleperson.printFullName()
femaleperson=FemalePerson()
femaleperson.setFirstName("Indira")
femaleperson.setLastName("Chakka")
femaleperson.printFullName()