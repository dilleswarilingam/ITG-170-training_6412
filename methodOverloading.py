class Demo:

    # First method
    def display(self, a):
        print("One argument:", a)

    # Second method with same name
    def display(self, a, b):
        print("Two arguments:", a, b)


# Creating object
obj = Demo()

# Calling method
obj.display(10, 20)