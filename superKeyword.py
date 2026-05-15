# Parent class
class Parent:

    def show(self):
        print("This is Parent class method")


# Child class
class Child(Parent):

    def show(self):
        super().show()   # calling parent class method
        print("This is Child class method")


# Creating object
obj = Child()

# Calling method
obj.show()