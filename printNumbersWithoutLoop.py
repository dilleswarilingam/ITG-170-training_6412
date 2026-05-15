def numbers(n):
    if n>0: 
        numbers(n-1)
        print(n)
n=100
numbers(n)