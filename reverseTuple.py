t1=(1,2,3,4,5)
rev=()
i=0
while i<len(t1):
    rev=(t1[i],)+rev
    i+=1

print(rev)