from abc import ABC, abstractmethod

# Abstract Class
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


# Child Class 1
class Dog(Animal):

    def sound(self):
        print("Dog barks")


# Child Class 2
class Cat(Animal):

    def sound(self):
        print("Cat meows")


# Creating objects
d = Dog()
c = Cat()

# Calling methods
d.sound()
c.sound()