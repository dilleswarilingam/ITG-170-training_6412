#sum of odd and even digits in a number 
num=int(input("Enter the number: "))
sum1=0
sum2=0
pos=1
while num>0:
    digit=num%10
    if pos%2==0:
        sum1=sum1+digit
    else:
        sum2=sum2+digit
    num=num//10
    pos=pos+1

print("The sum of even place digits is :",sum1)
print("The sum of odd place digits is: ",sum2)
