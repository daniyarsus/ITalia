
b = []
a = []

c, d = int(input()), int(input())
x = c/d
print(x)

x_str = str(x)
x_list = list(x_str)

i = 0
for i in range(len(x_str)):
    if x_str[i] == '.':
        break
    b.append(x_str[i])
x_str = x_str.replace(x_str[:(len(b)+1)], '')
a = list(x_str)
print(b, a)

a.reverse()
print(a)

i = 0
for i in range(len(a)):
    if i == len(a)-1:
        break
    if a[i] < a[i + 1]:
        print(a[i],'<', a[i+1])

        if int(a[i]) < 5:
            print(a[i],'<<',5)
            a[i + 1] = str(int(a[i + 1]))
        elif int(a[i]) > 5:
            print(a[i],'>>',5)
            a[i + 1] = str(int(a[i + 1]) + 1)
        else:
            print(a[i],'==',5)
            a[i + 1] = str(int(a[i + 1]) + 1)
    if a[i] > a[i + 1]:
        print(a[i],'>', a[i+1])

        if int(a[i]) < 5:
            print(a[i],'<<',5)
            a[i + 1] = str(int(a[i + 1]))
        elif int(a[i]) > 5:
            print(a[i],'>>',5)
            a[i + 1] = str(int(a[i + 1]) + 1)
        else:
            print(a[i],'==',5)
            a[i + 1] = str(int(a[i + 1]) + 1)

    if a[i] == a[i + 1]:
        print(a[i],'=', a[i+1])

        if int(a[i]) < 5:
            print(a[i],'<<',5)
            a[i + 1] = str(int(a[i + 1]))
        elif int(a[i]) > 5:
            print(a[i],'>>',5)
            a[i + 1] = str(int(a[i + 1]) + 1)
        else:
            print(a[i],'==',5)
            a[i + 1] = str(int(a[i + 1]) + 1)

a.reverse()
print(a)

if int(a[0]) < 5:
    print("".join(b))

elif int(a[0]) > 5:
    b[-1] = str(int(b[-1]) + 1)
    print("".join(b))

else:
    b[-1] = str(int(b[-1]) + 1)
    print("".join(b))