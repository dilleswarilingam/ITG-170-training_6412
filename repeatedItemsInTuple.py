t1=(1,2,3,2,4,1,5,6)
res=[]
for i in t1:
    if t1.count(i)>1 and i not in res:
        res.append(i)
print(res)