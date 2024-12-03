def power(n):
    s=0
    for i in range (1,(n+1),2):
        s+=i ** 2
    return s
print(power(10))