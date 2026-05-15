list1=[1,2,3,4,5,6,7]
sum=7
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]+list1[j]==sum:
            print(f"sum of {list1[i]} and {list1[j]} is equal to {sum}")