list1=[1,2,2,3,4,5,4,5,6,6,6,7]
list2=[]
list3=[]
for item in list1:
    if item in list2:
        list3.append(item)
    list2.append(item)
print("duplicate values:",list3)