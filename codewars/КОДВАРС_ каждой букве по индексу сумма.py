def words_to_marks(s):
    alfavit = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
    alfavitValue = {}
    sTrue = []
    k = 1
    for i in alfavit:
        alfavitValue.update({i:k})
        k += 1
    for i in range(len(list(s.lower()))):
        sTrue.append(alfavitValue.get(s[i]))
    return sum(sTrue)
print(words_to_marks('hzzzzzzzzzzzzzzzzzzzzzzzzzzh'))