def mode(sequence):
    repetitions = [0] * 4 * (len(sequence) + 1)
    max = 1
    k = sequence[0]

    for number in sequence:
        repetitions[number] += 1
        if repetitions[number] > max:
            max = repetitions[number]
            k = number
    
    return k

# sequence = [0, 1, 1, 2, 3, 4, 3, 5, 3, 2, 1]
# print(mode(sequence))