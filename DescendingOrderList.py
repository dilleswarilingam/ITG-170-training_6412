list1=[30,54,75,89,36]
list2=[]
while len(list1)>0:
    max=list1[0]
    for num in list1:
        if num>max:
            max=num
    list2.append(max)
    list1.remove(max)
print(list2)