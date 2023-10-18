def two_oldest_ages(ages):
    ages = list(set(sorted(ages)))
    oldests = [ages[-2], ages[-1]]
    return oldests
print(two_oldest_ages([1, 2, 5, 2]))
