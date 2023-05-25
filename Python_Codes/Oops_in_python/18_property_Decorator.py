class Employee:
    Company = "Google"
    Salary = 500
    Bonous = 200
    #totalSalary=700

    @property
    def totalSalary(self):
        return self.Salary + self.Bonous
    @totalSalary.setter
    def totalSalary(self,val):
        self.SalaryBonous = val-self.Salary

e = Employee()
print(e.totalSalary)
e.totalSalary=3000
print(e.Salary)
print(e.SalaryBonous)
