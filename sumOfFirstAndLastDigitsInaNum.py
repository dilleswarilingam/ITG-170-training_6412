num=int(input("Enter a number: "))
last=num%10
total=0
while num>=10:
    num=num//10

total=num+last
print(total)