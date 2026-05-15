#perfect number= sum of its proper divisors except itself is equal to the number itself
num=int(input("Enter a number: "))
sum=0
if num>1:
    for i in range(1,num):
        if num%i==0:
            sum+=i
    
    if sum==num:
        print(f"The number {num} is a perfect number")
    else:
        print(f"The number {num} is not a perfect number")
else:
    print(f"The number {num} is not a perfect number")