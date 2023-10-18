def alphabet_position(text):
    alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
    alphabetValue = {}
    textStr = []
    textSolution = []
    for i in text.lower():
        if i in alphabet:
            textStr.append(i)
    k = 0
    for i in alphabet:
        k += 1
        alphabetValue.update({i:k})
    for i in (''.join(textStr)):
        textSolution.append(alphabetValue.get(i))
    return ' '.join([str(i) for i in textSolution])
print(alphabet_position("The sunset sets at twelve o' clock."))