list1=[(10,20,30),(20,30,40),(30,40,50)]
list2=[]
for i in list1:
    list2.append(list(i))
    for j in list2:
        j[2]=100
print(list2)