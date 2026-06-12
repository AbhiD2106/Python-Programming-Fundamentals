class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):  # Overriding the parent method
        super().speak()  # Call parent method
        print("Dog barks")

d = Dog()
d.speak()