n = int(input("Enter the number of integers "))
numberArray = input("Enter the array's elements\n").split()

for i in range(0,n//2):
	numberArray[i], numberArray[len(numberArray)-i-1] = numberArray[len(numberArray)-i-1], numberArray[i]

print(*numberArray, sep = " ")
