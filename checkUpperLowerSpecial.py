demo=input("Enter a string with uppercase,lowercase and special characters:")
list1=[]
list2=[]
list3=[]
list4=[]
for ch in demo:
    #if ch.isupper():
    if ch>='A'and ch<='Z':
        list1.append(ch)
    #elif ch.islower():
    elif ch>='a' and ch<='z':
        list2.append(ch)
    #elif ch.isdigit():
    elif ch>='0' and ch<='9':
        list3.append(ch)
    else:
        list4.append(ch)

print(list1)
print(list2)
print(list3)
print(list4)