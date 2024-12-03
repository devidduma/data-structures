def oddSquare(n):
    s=0
    for i in range(1,n+1,2):
        s+=i*i
    return s
