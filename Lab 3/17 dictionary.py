dictionary = {}
stringValues = input("Enter string values separated by spaces\n").split()

for string in stringValues:
	if string not in dictionary:
		dictionary[string] = 1
	else:
		dictionary[string] += 1

print(dictionary)
