class Employee:
    Company="Visa"
    Salary=100
    location="Mumbai"

    @classmethod
    def ChangeSalary(cls,sal):
        cls.Salary=sal

e=Employee()
print(e.Salary)
e.ChangeSalary(344)
print(Employee.Salary)