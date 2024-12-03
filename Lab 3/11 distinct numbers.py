def checkIfAllDifferent(numberArray):
	
	for i in range(1, len(numberArray)):
		for j in range(i,0,-1):
			if numberArray[j-1] > numberArray[j]:
				numberArray[j-1], numberArray[j] = numberArray[j], numberArray[j-1]
			elif numberArray[j-1] == numberArray[j]:
				return False
			else:
				break
	
	return True

numberArray = input("Enter the numbers split by spaces\n").split()
print(checkIfAllDifferent(numberArray))
