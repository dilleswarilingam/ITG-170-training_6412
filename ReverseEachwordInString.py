str1="Hello welcome to python"
word=""
result=""
for ch in str1:
    if ch!=" ":
        word=ch+word
    else:
        result=result+word+" "
        word=""

result=result+word
print(result)