def unique_in_order(iterable):
    array = list(iterable)
    for i in range(len(array)):
        if i == len(array) - 1:
            break
        if array[i] == array[i + 1]:
            array.remove(array[i + 1])
    return array

print(unique_in_order('AAAABBBCCDDDAABBB'))