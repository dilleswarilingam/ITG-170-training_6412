s1="this is my string"
word=""
capitalize=True
for ch in s1:
	if ch==" ":
		word+=ch
		capitalize=True
	else:
		if capitalize and 'a'<=ch<='z':
			word+=chr(ord(ch)-32)
		else:
			word+=ch
            
		capitalize=False

print(word)