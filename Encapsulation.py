class Student:

    def __init__(self, name, age, marks):
        self.name = name          # Public
        self._age = age           # Protected
        self.__marks = marks      # Private

    # Getter method for private variable
    def get_marks(self):
        return self.__marks

    # Getter method for protected variable
    def get_age(self):
        return self._age


# Creating object
s1 = Student("Rahul", 20, 90)

# Accessing public variable directly
print("Name:", s1.name)

# Accessing protected variable using getter
print("Age:", s1.get_age())

# Accessing private variable using getter
print("Marks:", s1.get_marks())