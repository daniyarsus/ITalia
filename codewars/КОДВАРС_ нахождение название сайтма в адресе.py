def domain_name(url):
    name = []
    for i in range(len(url)):
        if url[i] == ('http://www.'):
            name.append(url[i + 1])
    return ''.join(name)
print(domain_name('http://www.zombie-bites.com'))