def likes(names_list):
    names = ' '.join(names_list)
    if len(names_list) == 1:
        names = f'{names} like this'

    elif len(names_list) == 2:
        names = names.replace(' ', ' and ')
        names = (f'{names} like this')

    elif len(names_list) == 3:
        names = f'{names_list[0]}, {names_list[1]} and {names_list[2]} like this'

    else:
        count = len(names_list) - 2
        names = (f'{names_list[0]}, {names_list[1]} and other {count} like this')

    return names
print(likes(['vova', 'andrey', 'bob']))