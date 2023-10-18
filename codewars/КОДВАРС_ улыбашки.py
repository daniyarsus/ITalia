def count_smileys(arr):
    eyes = [':', ';']
    noise = ['-', '~']
    mouth = [')', 'D']
    trueCount = []
    for index in range(len(arr)):
        if (len(arr[index]) == 2) and (arr[index][0] in eyes) and (arr[index][1] in mouth):
            trueCount.append(arr[index])
        elif (len(arr[index]) == 3) and (arr[index][0] in eyes) and (arr[index][1] in noise) and (arr[index][2] in mouth):
            trueCount.append(arr[index])
    return len(trueCount)
print(count_smileys([':D', ':~)', ';~D', ':)']))