list1=[1,2,3,6,4,7,9,9]
largest=list1[0]
smallest=list1[0]
for num in list1:
    if num >= largest:
        largest=num
    if num <= smallest:
        smallest=num
print(largest)
print(smallest)