list1=[1,2,3,4,5]
smallest=list1[0]
second_small=list1[0]
for num in list1:
    if num<smallest:
        smallest=num

for num in list1:
    if num>smallest and (second_small==smallest or num < second_small):
        second_small=num
print(second_small)