#ex3
def findNumberNotInSequence(S):
    sum=0 #o(1)
    n=len(S) #o(1)
    for i in S: #O(n) find the sum of array
sum+=i #o(1)
        return (int)(n*(n-1)/2-sum) #o(1) find the sum from 1 to n-1
#Output is 4
#Time complexity is O(n+3)=O(n)

