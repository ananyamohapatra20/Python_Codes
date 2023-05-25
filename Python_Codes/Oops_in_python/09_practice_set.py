class Programmer:
    company = "Microsoft"

    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getInfo(self):
        print(f"Name of the company {self.company} and the Programmer is {self.name} product is {self.product}")


obj1 = Programmer("Harry", "Skype")
obj2 = Programmer("Anu", "GitHub")
obj1.getInfo()
obj2.getInfo()
