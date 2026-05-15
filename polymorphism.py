# Parent class
class Animal:
    
    def sound(self):
        print("Animals make sounds")


# Child class 1
class Dog(Animal):

    def sound(self):
        print("Dog barks")


# Child class 2
class Cat(Animal):

    def sound(self):
        print("Cat meows")


# Creating objects
a = Animal()
d = Dog()
c = Cat()

# Polymorphism
a.sound()
d.sound()
c.sound()