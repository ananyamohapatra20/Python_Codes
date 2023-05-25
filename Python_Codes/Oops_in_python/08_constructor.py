class Employee:
    company="Google"

    def __init__(self, name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("Employee is created!! ")
    def getDetails(self):
        print(f"The name of the Employee {self.name}")
        print(f"Salary is {self.salary}")
        print(f"The subunit of the Employee {self.subunit}")

    def getSalary(self,sign):
        print(f"Salary for this employee in {self.company} is {self.salary}\n{sign}")

    @staticmethod
    def greet():
        print("Good Morning")


harry=Employee("Harry",100,"Youtube")
#harry=Employee("")---->This throws an error(missing 3 required prepositional arguments)
harry.getDetails()

