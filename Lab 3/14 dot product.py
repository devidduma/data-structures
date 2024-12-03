n = int(input("Enter length n\n"))
a = []
b = []

print("Enter values for array a separated by line break")
a = [ int(input()) for i in range(n)]

print("Enter values for array b separated by line break")
b = [ int(input()) for i in range(n)]

c = list()
for i in range(n):
	c.append(a[i]*b[i])

print("Result of dot product (c array)")
print(*c, sep= " ")
