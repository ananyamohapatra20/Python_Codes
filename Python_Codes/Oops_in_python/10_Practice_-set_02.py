class Calculator:
    def __init__(self,num):
        self.num=num

    def square(self):
        print(self.num**2)

    def Cube(self):
        print(self.num**3)

    def squareroot(self):
        print(self.num**0.5)

obj1=Calculator(9)
obj1.square()
obj1.Cube()
obj1.squareroot()