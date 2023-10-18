def move_zeros(array):
    other, zeros = [], []
    for i in array:
        if i > 0:
            other.append(i)
        else:
            zeros.append(i)
    return other + zeros

print(move_zeros([1, 0, 1, 2, 0, 1, 3]))