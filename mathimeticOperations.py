num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
def add(n1,n2):
    sum=n1+n2
    print(f"The sum {n1} and {n2} is {sum}")

def sub(n1,n2):
    diff=n1-n2
    print(f"The difference of {n1} and {n2} is {diff}")

def mul(n1,n2):
    product=n1*n2
    print(f"The product of {n1} and {n2} is {product}")

def div(n1,n2):
    if n1>n2:
        res=n1/n2
        print(f"The division of {n1} and {n2} is {res}")
    else:
        res1=n2/n1
        print(f"The division of {n1} and {n2} is {res1}")

add(num1,num2)
sub(num1,num2)
mul(num1,num2)
div(num1,num2)