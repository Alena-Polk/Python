from random import randint


def binary_search(s, item):
    last = len(s) - 1
    first = 0
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if s[midpoint] == item:
            found = True
        else:
            if item < s[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


a = [randint(1, 100) for i in range(10)]
print(a)
a.sort()
print(a)
n = int(input("Введите число: "))
if binary_search(a, n):
    print(f'Число {n} в списке присутствует')
else:
    print(f'Число {n} в списке отсутствует')