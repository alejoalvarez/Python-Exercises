# This is an example of inheritance


"""Class that represent a person."""
class Person(object):

    def __init__(self, identification, name, last_name):
        "Constructor"
        self.identification = identification
        self.name = name
        self.last_name = last_name

    def __str__(self):
        return " %s: %s, %s" %(str(self.identification), self.last_name, self.name)


"""Class that represent a Student"""
class Student(Person):

    def __init__(self, identification, name, last_name, age):
        "Constructor "
        # call constructor person
        Person.__init__(self, identification, name, last_name)
        # add new attributes
        self.age = age


a = Student(1234, "Alejo", "Alvarez", 12)
print(a)