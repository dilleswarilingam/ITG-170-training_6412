try:
    num1=int(input("Enter a number: "))
    num2=int(input("Enter a number: "))
    result=num1/num2
    print("result:",result)
    try:
        text=input("Enter your name : ")
        print("the name is: ",text)
        if text.isdigit:
            raise ValueError("Please give name not a number")
    except ValueError as e:
        print(e)
except ZeroDivisionError as e:
    print(e)
finally:
    print("The program completed")