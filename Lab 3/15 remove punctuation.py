stringin = input()
stringout = ""

for i in range(0, len(stringin)):
	if( (stringin[i] >= 'A' and stringin[i] <= 'Z') or
		(stringin[i] >= 'a' and stringin[i] <= 'z') or
		(stringin[i] == " ")
		): stringout += stringin[i]

print(stringout)
	
