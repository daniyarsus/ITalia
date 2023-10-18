def order(sentence):
    sentence = sentence.split()
    for index in range(len(sentence)):
        sentence[index][index] = '4'


print(order('4of Fo1r pe6ople g3ood th5e the2'))