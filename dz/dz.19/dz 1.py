from random import randint


def seq_search(s, item):
    pos = 0
    found = False
    while pos < len(s) and not found:
        if s[pos] == item:
            found = True
        else:
            pos += 1
    return found


spisok = [randint(1, 100) for i in range(10)]
print(spisok)
user = int(input("Введите число: "))
if seq_search(spisok, user):
    print(f'Число {user} в списке присутствует')
else:
    print(f'Число {user} в списке отсутствует')

