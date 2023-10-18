def sum_digits(number):
    str_sum_digits = [int(i) for i in str(number).replace('-', '')]
    return sum(list(str_sum_digits))
print(sum_digits(-12))