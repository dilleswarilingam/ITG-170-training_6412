# Parent class
class Employee:
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(self.name, "is working.")

    def getSalary(self):
        print("Salary of", self.name, "is", self.salary)


# Subclass
class HRManager(Employee):

    # Overriding work() method
    def work(self):
        print(self.name, "is managing HR tasks.")

    # New method
    def addEmployee(self, employee_name):
        print(employee_name, "has been added to the company.")


# Creating object of HRManager
hr = HRManager("Anita", 70000)

# Calling methods
hr.work()
hr.getSalary()
hr.addEmployee("Ravi")