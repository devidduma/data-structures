import random

def myShuffle(l):
	
	for i in range(len(l)):
		newItemIndex = random.randint(i, len(l)-1)
		l[i], l[newItemIndex] = l[newItemIndex], l[i]
