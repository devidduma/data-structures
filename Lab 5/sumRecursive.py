def sumRecursive(n):
	if(n == 1):
		return 1
	return n + sumRecursive(n-1)

number = int(input("Enter an integer between 1 to 100: "))
sum = sumRecursive(number)
print("Sum of numbers from 1 to ", number, " is ", sum)
