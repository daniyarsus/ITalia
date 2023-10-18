def duplicate_encode(word):
    word = word.lower()
    dict = {}
    for i in word:
        if word.count(i) == 1:
            dict.update({i:'('})
        else:
            dict.update({i:')'})
    return ''.join([dict.get(i) for i in word])
print(duplicate_encode('(( @'))