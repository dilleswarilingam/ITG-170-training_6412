set1={1,2,3,4,5,6}
list1=list(set1)   #max=min=next(iter(str1))
max=min=list1[0]
for num in list1:
    if num > max:
        max=num
    if num<min:
        min=num
print(max)
print(min)

