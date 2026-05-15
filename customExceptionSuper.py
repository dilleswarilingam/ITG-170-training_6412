class InvalidAgeException(Exception):
    def __init__(self, message):
        super().__init__(message)

try:
    age=int(input("Enter your age : "))
    if age<18:
        raise InvalidAgeException("you are not allowed to vote!")
    else:
        print("you can vote")
except InvalidAgeException as e:
    print(e)
except ValueError as e:
    print(e)