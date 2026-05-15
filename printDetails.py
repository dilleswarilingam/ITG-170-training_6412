from datetime import datetime
name=input("Enter your name : ")
city=input("Enter your city: ")
today=datetime.now()
todaysDate=today.strftime("%d %B %y")
day=today.strftime("%A")
age=int(input("Enter your age: "))
print(f"My name is {name} and I am from {city},my age is {age}")
print(f"today's date is {todaysDate} {day}")
