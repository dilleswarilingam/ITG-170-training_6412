num=int(input("Enter a number: "))
last_digit=num%10
same=True
while num>0:
    digit=num%10
    if digit!=last_digit:
        same=False
    num=num//10

if same:
    print("All the digits are same.")
else:
    print("All the digits are not same.")