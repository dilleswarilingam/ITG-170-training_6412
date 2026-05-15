list1=[1,2,2,3,4,5,4,5,6,6,6,7]
list2=[]
for item in list1:
    if item in list2:
        continue
    count=0
    for x in list1:
        if item==x:
            count+=1
    list2.append(item)
    print(f"The item {item} is occured {count} times")

