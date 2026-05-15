list1=[1,2,3,4,5,6,7,8]
res=any(num<5 for num in list1)
res1=all(num<5 for num in list1)
print(res)
print(res1)