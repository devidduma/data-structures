def first_n_Fibonacci_numbers(n):
    if(n <= 0):
        return []
    elif(n == 1):
        return [1]

    numbers = [1, 2]
    for i in range(2,n):
        numbers.append(numbers[i-1] + numbers[i-2])
    
    return numbers

# print(first_n_Fibonacci_numbers(10))