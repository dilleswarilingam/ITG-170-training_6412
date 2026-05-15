class Employee:
    
    # Constructor
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Method to display work
    def work(self):
        print(self.name, "is working.")

    # Method to display salary
    def getSalary(self):
        print("Salary of", self.name, "is", self.salary)


# Creating object
emp1 = Employee("Ravi", 50000)

# Calling methods
emp1.work()
emp1.getSalary()