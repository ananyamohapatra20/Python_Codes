class Employee:
    company="Google"
    def getSalary(self,sign):
        print(f"Salary for this employee in {self.company} is {self.salary}\n{sign}")
    @staticmethod
    def greet():
        print("Good Morning")
harry=Employee()
harry.salary=10000
harry.getSalary("Thanks! ")
harry.greet()