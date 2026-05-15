list1=[10,23,34,45,57,89,88]
list2=[]
list3=[]
for num in list1:
    if num%2==0:
        list2.append(num)
    else:
        list3.append(num)
print("The even numbers are: ",list2)
print("The odd numbers are : ",list3)