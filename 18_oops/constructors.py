class Employee:
    def __init__(self,name,age,salary,bond):   
        self.name = name    #self represent current object , self like this keyword in java
        self.age = age
        self.salary = salary
        self.bond = bond
        

    def emp_details(self):
        return self.name,self.age
    
    def information(self):
        print("Employee Name:",self.name,"Age:",self.age,"Salary:",self.salary,"Bond:",self.bond)

e1 = Employee("John",25,50000,2)   #object creation
print(e1.emp_details())    #accessing method using object
e1.information()           #accessing method using object