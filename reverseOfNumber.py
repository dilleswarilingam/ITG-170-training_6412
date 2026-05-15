num=int(input("Enter a number: "))
rev=""
word=str(num)
for ch in word:
    rev=ch+rev

res=int(rev)
print(res)