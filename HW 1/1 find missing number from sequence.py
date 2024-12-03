def find_missing_number_from_sequence(sequence):
    current_sum = 0.0
    n = len(sequence) + 1
    total_sum = n*(n-1)/2

    for s in sequence:
        current_sum += s
    
    missing_number = total_sum - current_sum
    return missing_number

# sequence = [0,1,2,4,5,6,7]
# print(find_missing_number_from_sequence(sequence))