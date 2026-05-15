num=int(input("Enter a number: "))
digit=int(input("Enter a digit that u want to search for: "))
count=0
while num>0:
    res=num%10
    if res==digit:
        count=count+1
    num=num//10

print(f"The digit {digit} is occured in the number {count} times.")