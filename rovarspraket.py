# dailyprogrammer 

# swedish letters:
# ALT+0197, ALT+0229, ALT+0196, ALT+0228, ALT+0214, ALT+0246
# but my powershell can't actally handle it, so i'm not coding them in

import string

consonants = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
vowels = ['a','e','i','o','u','y']

s = str(raw_input())
newString = ''
for i in s:
	if i in consonants:
		if i in string.ascii_uppercase:
			newString = newString+ i+'o'+i.lower()
		else:
			newString = newString+i+'o'+i
	else:
		newString = newString + i
print newString
