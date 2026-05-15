num=int(input("Enter the number: "))
sum=0
while num>0:
    digit=num%10
    sum+=digit
    num=num//10
print(sum)

#using recurssion 
def sum_digits(n):
    if n==0:
        return 0
    else:
        return(n%10)+sum_digits(n//10)
    
num=int(input("Enter a number: "))
print(sum_digits(num))