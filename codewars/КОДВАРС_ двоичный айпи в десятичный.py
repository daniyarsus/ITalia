def is_valid_IP(string):
    ip = []
    for i in string.split('.'):
        if int(i, 2) in range(0, 255):
            ip.append(str(int(i, 2)))
    return '.'.join(ip)
print(is_valid_IP('101.1000.1000000.1001101'))