class Student:
    Name = "John"

    def get_age(self):          #self is a default parameter which represent current object
        print(self)             #it will print address of current object
        return 20
    
s2 = Student()          #object creation
print(s2.get_age())       #accessing method using object
print(s2.Name)          #accessing attribute using object