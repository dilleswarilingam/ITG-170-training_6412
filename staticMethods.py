class Calculator:

    @staticmethod
    def add(a, b):
        print("Sum =", a + b)

    @staticmethod
    def multiply(a, b):
        print("Product =", a * b)


# Calling static methods (no object needed)
Calculator.add(10, 20)
Calculator.multiply(5, 4)