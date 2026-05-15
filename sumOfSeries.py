num=int(input("Enter the number: "))
sum=0
#1+1/2+1/3+...+1/n
for i in range(1,num+1):
    sum=sum+(1/i)
print(sum)
#1+1/2^2+1/3^2+...+1/n^2
for i in range(1,num+1):
    sum=sum+(1/i**2)
print(sum)
#1/1^0+1/2^1+1/3^2+....+1/n^n-1
for i in range(1,num+1):
    sum=sum+(1/i**(i-1))
print(sum)
#1/2^0+1/2^1+1/2^2+....+1/2^n
for i in range(0,num+1):
    sum=sum+(1/2**i)
print(sum)
#1/1!+1/2!+1/3!+....+1/n!
for i in range(1,num+1):
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    sum=sum+(1/fact)
print(sum)