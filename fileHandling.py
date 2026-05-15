with open("example.txt","w") as file:
    file.write("how are you ")

with open("example.txt","r") as file:
    res=file.read()
    print(res)

with open("example.txt","a") as file:
    file.write("\nhow was the day")

with open("example.txt","r") as file:
    result=file.read()
    print(result)
#split()--- copy the words in a list format
with open("example.txt","r") as file:
    res=file.read()
    words=res.split()
print(words)
print(len(words))

find_word="day"
with open("example.txt","r") as file:
    res=file.read()
    words=res.split()
    if find_word in words:
        print("word found")
    else:
        print("The file not found")
#strip()---this will remove white spaces at begining and ending and remove \n as 
#new line already contains it 
count=0
with open("example.txt","r") as file:
    lines=file.read()
    words=lines.split()
    for line in words:
        print(line.strip())
        count+=1
print(count)


#print lines ina list format 
with open("example.txt","r") as file:
    lines=file.read()
    words=lines.split()
    print(words)