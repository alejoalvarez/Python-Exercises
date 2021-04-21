# This is an example of inheritance


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_message(self):
        print("Name: ", self.name)
        print("Age: ", self.age)


class Employee(Person):

    def __init__(self, salary):
        super().__init__("Alejo1", "Alvarez1")
        self.salary = salary

    def __str__(self):
        properties = "Name: " + self.name + " Age: " + self.age + " Salary: " + str(self.salary)
        return properties


person1 = Person("Alejo", "Alvarez")
person1.print_message()
print("-------------------")
employee1 = Employee(1000)
print(employee1)
