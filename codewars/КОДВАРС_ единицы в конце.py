def increment_string(strng):
    array = []
    for i in strng:
        if i.isdigit():
            array.append(str(int(i) + 1))
        else:
            array.append(i)
    return ''.join(array)

print(increment_string('defile99'))