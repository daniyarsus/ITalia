#def can_get_to_N(start, N):
#    if start == N:
#        return "YES"
#    elif start > N:
#        return "NO"
#    # Пробуем два варианта: добавить 3 и добавить 5
#    return can_get_to_N(start + 3, N) or can_get_to_N(start + 5, N)
#
#
#N = int(input("Введите число N: "))
#result = can_get_to_N(1, N)
#print(result)

def max_number(n, k):
    for i in range(len(str(k))):
        if n > k[i]:
            n = k
        else:
            continue
    return n


