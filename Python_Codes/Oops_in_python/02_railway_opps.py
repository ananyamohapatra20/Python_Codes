class RailForm:
    form="RailForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")
application=RailForm()
application.name="MUNU"
application.train="Rajdhani"
application.printData()