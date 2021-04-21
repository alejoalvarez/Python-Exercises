# This is an example for a class


class Person:

    def initializer(self, nom, lastName):
        self.name = nom
        self.lastName = lastName


    def print_message(self):
        print("Name: ", self.name, self.lastName)


person1 = Person()
person1.initializer("Alejo", "Alvarez")
person1.print_message()


person2 = Person()
person2.initializer("Pepito", "Perez")
person2.print_message()


# Method init (constructor)
class Person2:

    def __init__(self, nom, lastName):
        self.name = nom
        self.lastName = lastName


    def print_message(self):
        print("Name: ", self.name)
        print("LastName: ", self.lastName)


person1 = Person2("Alejo", "Alvarez")
person1.print_message()


person2 = Person2("Pepito","Perez")
person2.print_message()
