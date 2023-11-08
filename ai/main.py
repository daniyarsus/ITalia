x = input()
r = []
print(r)
for i in x:
    if i.isdigit():
        r.append(i)
    else:
        continue
print(r)
print(len(r))