list1=["hi","hello","world"]
res=[i for i in list1  if len(i)>3]
print(list(res))

#with filter()
res1=list(filter(lambda x:len(x)>3,list1))
print(res1)