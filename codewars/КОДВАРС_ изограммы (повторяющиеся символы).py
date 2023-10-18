def is_isogram(string):
    for i in range(len(string)):
        if string[i].isdigit():
            return False

    if len(string) == len(set(string)):
        return True
    else:
        return False

print(is_isogram('hela'))