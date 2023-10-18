def accum(s):
    list_accum = []
    for i in range(len(s)):
        list_accum.append(s[i].upper() + s[i].lower() * i)
    str_accum = "-".join(list_accum)
    return str_accum
print(accum('aBcdEfhhhhhH'))