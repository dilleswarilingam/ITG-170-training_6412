#sum of squares of its digits finally reach to 1 
#19=1^2+9^2  =82 =8^2+2^2  =68  =6^2+8^2 =100 = 1^2+0^2+0^2  =1 happy number
num=int(input("Enter a number: "))
seen=[]
while num!=1 and num not in seen:
    seen.append(num)
    sum=0
    while num>0:
        digit=num%10
        sum=sum+digit**2
        num=num//10
    num=sum

if sum==1:
    print("happy number")
else:
    print("Not happy number")

print(seen)#optional