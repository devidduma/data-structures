#ex5
n=3
S=[[2]*n]*n
s=0
for i in range(n):#we find the sum by using 2 for loops
  for j in range(n):
    s+=S[i][j]
print(s)
