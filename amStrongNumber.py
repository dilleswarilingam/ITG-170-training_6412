#number is equal to cube of its digits 
for num in range(1,1001):
    result=0
    temp=num
    while temp!=0:
        digit=temp%10
        result+=digit**3
        temp=temp//10
    if result==num:
        print(num)