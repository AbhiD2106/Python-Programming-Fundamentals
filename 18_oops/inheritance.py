class car:
    location = "Germany"
    def __init__(self,name):
        self.name = name

    def audi(self):
        print("Audi is a German Car...")

class Bmw(car):
    def drive(self):
        print("BMW also german car")
        print("Car name is:",self.name)  #accessing parent class attribute using child class object

a = Bmw("mercedes") #object creation of child class 

a.audi()
a.drive()
print(a.location)       #accessing parent class attribute using child class object