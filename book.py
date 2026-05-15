price=int(input("Enter the price of the book you want: "))
quantity=int(input("Enter how many books you want: "))
total=price*quantity
if quantity<2 and quantity>0:
    print(f"you wanted a book of cost {price} so the total bill is {total}")
else:
    print(f"you wanted {quantity} books of cost {price} so the total bill is {total}")