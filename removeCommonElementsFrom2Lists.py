list1=[1,2,3,4,5]
list2=[3,4,5,6,7]
res1=[]
res2=[]
for num in list1:
    if num not in list2:
        res1.append(num)

for num in list2:
    if num not in list1:
        res2.append(num)
print(res1)
print(res2)
