class Person:
    def __int__(self):
        print("Initializing Person ")
    country = "India"

    def takeBreath(self):
        print("I am breathing...")


class Employee(Person):
    company = "Honda"

    def __int__(self):
        super().__init__()
        print("Initializing Employee::: ")
    

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee so I am luckily breathing")


class Programmer(Employee):
    company = "Youtube"

    def getSalary(self):
        print(f"No salary to Programmers")

    def takeBreath(self):
        super().takeBreath()
        print("I am an Programmer so I am luckily breathing++ ")


a = Person()
a.takeBreath()

e = Employee()
e.takeBreath()

p = Programmer()
p.takeBreath()
