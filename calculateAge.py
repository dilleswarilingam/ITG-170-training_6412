birthDate=int(input("Enter your birth year: "))
age=2026-birthDate
print(f"Your age is {age}")

#using datetime
from datetime import datetime
birthDate=int(input("Enter your birth year: "))
demo=datetime.now()
currDate=int(demo.strftime("%Y"))
age=currDate-birthDate
print(f"Your age is {age}")