def oddProduct():

	numberArray = list(map(int, input("Enter number sequence separated by spaces\n").split()))
	
	for i in range(len(numberArray)):
		for j in range(i, len(numberArray)):
			if(numberArray[i]%2==1 and numberArray[j]%2==1 and numberArray[i]!=numberArray[j]):
				return True
	return False
	
print(oddProduct())
