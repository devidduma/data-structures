def minmax():
	numberArray = input("Enter number sequence: ").split()
	min = int(numberArray[0])
	max = 0
	for i in range(len(numberArray)):
		if int(numberArray[i]) < min:
			min = int(numberArray[i])
		elif int(numberArray[i]) > max:
			max = int(numberArray[i])
	
	return min, max

#print(minmax())
