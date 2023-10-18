def maskify(cc):
    if len(cc) <= 4:
        return cc
    elif len(cc) > 4:
        return ('#' * (len(cc) - 4)) + cc[-4:]
print(maskify('4532030123'))