class Employee:
    company = "Google"
    salary=100
anu= Employee()
Munu= Employee()
anu.salary=300
Munu.salary=400
print(anu.company)
print(Munu.company)
#Directly assiciated #Class Attribute
Employee.company="YouTube"
print(anu.company)
print(Munu.company)
print(anu.salary)
print(Munu.salary)
