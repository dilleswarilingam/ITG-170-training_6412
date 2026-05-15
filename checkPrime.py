num=int(input("Enter a number: "))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("The given number is not a prime number")
            break
    else:
        print("The given number is a prime number")
else:
    print("The given number is not a prime number")