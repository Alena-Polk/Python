# name_new = "Elena"
# age = 20
# print("Hello,", name_new)
# print(type(age))

# a = b = c = 1
# print(a, b, c)
#
# a, b, c = "Hello", 5, False
# print(a, b, c)
#
# PI = 3.14
# print(PI)
# PI = 2
# print(PI)


# a = "hello"
# print(a)
# print(type(a))
# a = 5
# print(a)

# name = "Ольга"
# age = 21
# print("Меня зовут" + name + ". Мне " + str(age))

# a = 1
# b = 2
# print("a:", a)
# print("b:", b)
# a, b = b, a
# print("a:", a)
# print("b:", b)

# print("Строка \
#  символов")
# print('Строка символов')

# print("Документ \"file.py\" \tнаходится по заданному пути \nD:\\Python\\file.py")
#
# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ", " + s2 + "!\t\t"
# print(s3)
# print(s3 * 3)

# print(4545454647484846474848)
# print(4.545454647484846474848)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 / 2)    #3.0
# print(6 // 2)    #3
# print(6 ** 2)
# print(7 % 2)


# a = 5
# b = 7
# c = 3
# print("Сумма:", a + b + c)
# print("Сумма:", a * b * c)
# print("Среднее арифметическое:", (a+b+c)/3)

# number = 6+4*5**2+7
# print(number)
#
# number = (6 + 4) * (5 ** 2 + 7)
# print(number)

# num = 10
# num += 5  #num = num + 5
# print(num) #15
#
# num -=3  #num = num - 3
# print(num) #12
#
# num *=4 #num = num * 4
# print(num) #48

# num = 4321
# a = num % 10
# print(a)
# num = num//10
# # print(num)
# b = num % 10
# print(b)
# num = num//10
# # print(num)
# c = num % 10
# print(c)
# num = num//10
# # print(num)
# d = num % 10
# print(d)
# print(a * 1000 + b * 100 + c * 10 + d)

# num = 4321
# res = num % 10 * 1000
# num //= 10
# res += num % 10 * 100
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print()
#
# print(num)

# a = [1, 2, 3]
# b = [11, 22, 33]
# c = []
# print("a = ", a)
# print("b = ", b)
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# print(c)


# a = [1, 2, 3]
# b = [11, 22, 33, 4, 2]
# c = []
# print("a = ", a)
# print("b = ", b)
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):     #range(3, 5)
#     c.append(b[i])
# print(c)

# a = [1, 2, 3, 4, 2, 55, 99]
# b = [11, 22, 33, 14]
# c = []
# print("a = ", a)
# print("b = ", b)
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):     #range(3, 5)
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):     #range(5, 3)
#         c.append(a[i])
# print(c)


# a = [1, 2, 3, 4, 2, 55, 99]
# print(a)
# a.remove(2) #удаляет из списка указанный элемент по значению.# Если элементов несколько, удалится только первый.
# print(a)
# last = a.pop() #удаляет последний элемент из списка и возвращает удаляемое значение.
# print(last)
# print(a)
# last = a.pop(-2) #удаляет элемент по индексу и возвращает удаляемое значение.
# print(last)
# print(a)
# a.clear() #удаляет из списка все элементы
# print(a)

# a = [int(input("-> ")) for i in range(int(input("Введите элементы списка: ")))]
# k = int(input("Введите индекс: "))
# a.pop(k)
# print(a)


# a = []
# [a.append(input("->")) for i in range(int(input("n = ")))]
# print(a)
# while True:
#     if len(a)==0:
#     a.pop(k)
#     if not a:
#        break
#
#     print(a)

# a = [9, 5, 9, 7, 6, 9, 4, 9, 0, 9]
# print(a)
# num = a.count(9) #считает количество заданных значений в списке
# print(num)
# ind = a.index(7) #возвращает индекс первого вхождения взаданного значения.
#                  #Если значение не найдено, то будет исключение ValueError
# print(ind)
# ch = 7
# if ch in a:
#     ind = a.index(ch)
#     print(ind)

# a = [5, 9, 7]
# b = a
# print("a=", a)
# print("b=", b)
# b.append(120)
# print("a=", a)
# print("b=", b)
# print(id(a))
# print(id(b))


# a = [5, 9, 7]
# b = a.copy()
# print("a=", a)
# print("b=", b)
# b.append(120)
# print("a=", a)
# print("b=", b)
# print(id(a))
# print(id(b))

# a = [5, 9, 7, 6, 9, 4, 9, 0, 9]
# print(a)
# a.reverse() #переместили элементы списка в обратном порядке
# print(a)
# # a.sort() #сортирует элементы списка по умолчанию по возрастанию
# # print(a)
# a.sort(reverse=True) #сортирует элементы списка по убыванию
# print(a)
#
# b = sorted(a)
# print("b=", b)
# print("a=", a)
#
# # s = ['Виталий', 'Сергей','Александр', 'Анна']
# # print(s)
# # s.sort() #сортировка по алфавиту
# # print(s)
#
# # s = ['Виталий', 'Сергей','Александр', 'Анна']
# # print(s)
# # s.sort(key=len, reverse=True)
# # print(s)


# Генерация случайных данных

# import random
#
# print(random.random())
# print(random.randint(1, 9))# генерация случайного числа от заданного значения
#                           # до заданного значения включительно
#
# print(random.randrange(9))# генерация случайного числа от 0
#                           # до 9 ( 9-не включительно)
#
# print(random.randrange(2, 9)) # генерация от 2 до 9 ( 9-не включительно)
#
# print(random.randrange(0, 10, 2)) #генерация с интервалом 2, от 2 до 10.
#                                # ( 10-не включительно)


# from random import randint, randrange
#
# print(randint(1, 9))
# print(randrange(9))

# from random import *
# print(randint(1, 9))
# print(randrange(9))

# import random as r #импорт должен находиться в верху файла
#
# print(r.randint(1, 9))
# print(r.randrange(9))
# print(r.uniform(10.5, 25.5))#используется для генерации вещественного значения


# city = ['Москва','Новосибирск', 'Воронеж', 'Сочи', 'Екатеренбург']
# print(r.choice(city))
# print(r.choices(city, k=3))
# r.shuffle(city) #случайным образом перемешивает элементы списка
# print(city)

# city = [3, 5, 7, 8, 9]
# print(r.choice(city))
# print(r.choices(city, k=3))
# r.shuffle(city) #случайным образом перемешивает элементы списка
# print(city)

# mas = [input("->") for i in range(10)]
# print(mas)

# mas = [r.randint(50, 100) for i in range(20)]
# print(mas)

# mas = [r.randint(1, 20) for i in range(5)]
# print(mas)

# lst = [4, 6, 8, 9, 1]
# print(min(lst))
# print(max(lst))
# print(sum(lst))

# mas = [r.randint(1, 20) for i in range(10)]
# print(mas)
# b = max(mas)
# print(b)
# mas.remove(b)
# mas.insert(0, b)
# print(mas)

# a = [r.randint(-20, 20) for i in range(10)]
# print(a)
# a.sort(reverse=True)
# print(a)

# list_ = [r.randint(0, 100) for _ in range(10)]
# print(list_)
# min_ = min(list_)
# print('Min:', min_)
# index_min = list_.index(min_)
# print('Index min:', index_min)
# list_ = list_[index_min:]
# print(list_)

# x = list('1a2b3c4d')
# print(x)
# print('a'not in x)
# print('e'not in x)

# lst = []
# if len(lst) == 0:
#     print("Список пустой")
#
# if not lst:
#     print("Список пустой")

#
# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(m)
# # print(len(m))
# # print(m[1][2])
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()
# print()
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()

# for row in m:
# for x in row:
# print(x**2, end="\t")
# print()


# w, h = 10, 10
# matrix = [[x*y for x in range(1, w)] for y in range(1, h)]
# # matrix=[]
# for y in range(h):
#     new_row = []
#     for x in range(w):
#         new_row.appen(0)
#         matrix.append(new_row)
# print(matrix)
# for h in matrix:
#     for w in h:
#         print(w, end="\t\t")
#     print()
# print()

#
# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x + y)


# import random
#
# n = int(input("Введите размерность матрицы: "))
# mas = []
# for i in range(n):
#     mas.append([])
#     for j in range(n):
#         mas[i].append(random.randint(1, 100))
# print(mas)
# for row in mas:
#     for x in row:
#         print(x, end="\t")
#     print()
# print()
# m = 101
# lst = []
# for k in range(n):
#     if m > mas[k][k]:
#         lst.append(mas[k][k])
# print(lst, end="\t")
# print("\n", min(lst))

# import math      или
# from math import ceil или *

# num1 = math.ceil(3.2)
# num2 = math.floor(3.8)
# num3 = math.sqrt(2)
# print(num1)
# print(num2)
# print(num3)
# print(math.pi)

# from math import pi
# r = int(input("Введите длину окружности: "))
# d = pi*r*r
# print("Длина окружности: ", round(2*pi * r, 2))

import time

# second = time.time()
# print(second)
# a = 171522089
# local_time = time.ctime()
# print(local_time)
# res = time.localtime()
# print(res)
# print(res.tm_mon, res.tm_year)
# print(time.strftime("Today is %B %d, %Y"))
# print(time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime(a)))

# pause = 2
# print("Запуск программы")
# time.sleep(pause)
# print(pause, "сек.")

# text = input("Название напоминания: ")
# locale_time = float(input("Через сколько минут: "))
# locale_time = locale_time * 60
# time.sleep(locale_time)
# print(text)

# start = time.time()
# time.sleep(5)
# finish = time.time()
# res = finish - start
# print(res)

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)

# import locale
#
# locale.setlocale(locale.LC_ALL, "ru")
#
# print(time.strftime("Сегодня %B %d, %Y"))

# Функции
# a = 20
#
#
# def hello(name, age):
#     print("Hello, ", name, ". I am ", age, sep = "")
#
#
# hello("Irina", 20)
# hello("Ivan", 26)

# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# get_sum('abc', 'hello')
# get_sum(2.5, 4.3)


# def func(n, a, b):
#     for i in range(n):
#         if i % 2:
#             print(b, end = '')
#         else:
#             print(a, end='')
#     print()
#
# func(9, "+", '-')
# func(7, "X", "0")

# def get_sum(a, b):
#    if a > b:
#        return True
#    else:
#         return False
#
#
# x = 35
# y = 24
# if get_sum(x, y):
#     print(x, "больше", y)
# else:
#     print(y, "больше", x)

# def razn(a, b):
#     if a > b:
#         return a - b
#     else:
#         return a + b
#
#
# a, b = int(input("a = ")), int(input("b = "))
# print(razn(a, b))

# def cube(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, " в кубе =", cube(i))

#
# def change(lst):
#     lst[-1], lst[0] = lst[0], lst[-1]
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))


# def change(lst):
#     n = lst.pop()
#     m = lst.pop(0)
#     lst.insert(0, n)
#     # lst.append(m)
#     lst.insert(100, m)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))

#
# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         if "a" <= ch <= "z":
#             has_lower = True
#         if '0' <= ch <= "9":
#             has_num = True
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надежный пароль.")
# else:
#     print("Это ненадежный пароль")

# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))


# def set_param(c=20, s="-"):
#     for i in range(c):
#         print(s, end="")
#     print()
#
# set_param(10, s="+")
# set_param(5, '*')
# set_param(7)

# def digits_sum(n, even = True):
#     s = 0
#     while n > 0:
#         num = n % 10
#         if even and num % 2 == 0:
#             s += num
#         if not even and num % 2 != 0:
#             s += num
#         n //= 10
#     return s
#
# print('Сумма четных цифр:')
# print(digits_sum(9874023))
# print(digits_sum(38271))
# print(digits_sum(123456789))

# print('Сумма нечетных цифр:')
# print(digits_sum(9874023, even = False))
# print(digits_sum(38271, even = False))
# print(digits_sum(123456789, even = False))

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(id(lt1))
# print(id(lt2))
#
# print(lt1 == lt2)
# print(lt1 is lt2) #проверяет одинаковый ли адрес у переменных

# a = "Hello"
# b = "Hello" #одинаковый id у списков. не изменяемый тип данных
# print(id(a))
# print(id(b))
#
# print(a == b)
# print(a is b)

# строковое значение, числовое и вещественное число, не изменяемый тип данных
# "Hello", 3, 3.2, True
# списки, изменяемый тип данных

# s = "Hello"
# print(s, id(s))
# s = s + "World"
# print(s, id(s))
# # строки перезаписать нельзя, будет новый id

# a = 5
# print(a, id(a))
# a+= 1
# print(a, id(a))
# числа не измменяемый тип данных,
# перезаписать значение нельзя, будет новый id

# s = "Hello"
# print(s, id(s))
# s = s[1:-1]
# print(s, id(s))

# def add_number(n):
#     print("Внутри функции:", n, id(n))
#     n = n + [4]  # n += 4
#     print("Измененное значение:", n, id(n))
#
# x = [1, 2, 3]
# print("До функции:", x, id(x))
# m = add_number(x)
# print("После функции:", x, id(x))

# Кортеж (tuple)
# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst)
# print(tpl)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = ()
# print(type(a))
# b = tuple()
# print(type(b))

# a = (1, 2, 3, 4, 5)
# print(a, type(a))
# c = 1, 2, 3, 4, 5
# print(type(c))
# b = tuple(c)
# print(b, type(b))
#
# t = 1,
# print(type(t))


# a = (1, 2, 3, 4, 5)
# print(a)
# print(a[3])
# print(a[1:3])
# print()

# s = tuple(int(input("->")) for i in range(3))
# print(s)
from random import randint

# s = [randint(1, 20) for i in range(6)]
# print(tuple(s))

# s = tuple(randint(1, 20) for i in range(6))
# print(s)

# s = tuple(2 ** i for i in range(1, 13))
# print(s)

# t1 = tuple('hello')
# t2 = tuple('world')
# t3 = t1+t2
# print(t3)
# print(len(t3))
# print(t3.count('l'))
# print(t3.count('a'))
# print(t3.index("l", 4))
#
# if 'a' in t3:
#     print(t3.index("a"))
# else:
#     print('Такого символа нет')

# for i in t3:
#     # print(i, end=" ")
#     print(i * 2, end=" ")
# print('\n', t3)

# for i in range(len(t3)):
#     # print(i, end=" ")
#     print(t3[i] * 2, end=" ")
# print('\n', t3)

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             # return tpl[tpl.index(el):tpl.index(el, tpl.index(el) + 1) + 1]
#             start = tpl.index(el)
#             second = tpl.index(el, tpl.index(el) + 1)
#             return tpl[start:second + 1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# from random import randint
#
#
# def tuple_func(start, end):
#     return tuple(randint(start, end) for _ in range(10))
#
#
# tuple_1 = tuple_func(0, 5)
# tuple_2 = tuple_func(-5, 0)
# tuple_3 = tuple_1 + tuple_2
# count_0 = tuple_3.count(0)
#
# print(tuple_1)
# print(tuple_2)
# print(tuple_3)
# print('Count 0:', count_0)

# t = (10, ' Hello', [1, 2, 3], (4, 5, 6), ['hello', 'world'])
# print(t, id(t))
# t[-1][0] = 'new'
# print(t, id(t))

# Множество (set)

# s ={"banana", "apple", "orange", "apple"}
# print(type(s))
# print(len(s))
# print(s)

# a = set()
# print(type(a))

# a = set("Hello")
# print(type(a))
# print(a)

# b = ["Hello", "Hi"]
# a = set(b)
# print(type(a))
# print(a)

# s = {x for x in range(10)}
# print(s)

# s = {x*x for x in range(10)}
# print(s)

# numbers = [1, 2, 2, 2, 3, 3, 4, 4, 5, 6]
# # num = {i for i in numbers if i % 2 == 0}
# # num = set(numbers)
# num = list(set(numbers))
# print(num)

# def to_set(s):
#     st = set(s)
#     # print(s)
#     # return set(s), len(set(s))
#     return st, len(st)
#
#
# s_ = 'я обычная строка'
# lst = [4, 5, 4, 6, 2, 9, 11, 3, 4, 2]
# print(to_set(s_))
# print(to_set(lst))

# t = {'red', 'green', 'blue'}
# # print('green' in t)
# print('green' not in t)

# pr = {2, 5, 3, 7, 11}
# for i in pr:
#     print(i, end=' ')

# s = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in s if i[1] == 'c'}
# # a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in s}
# # a = {i for i in s if 'a' not in i}
# print(a)


# a = {0, 1, 2, 3}
# a.add(4)  # добавление элемента
# print(a)
# if 1 in a:
#     a.remove(1)  # удаление элемента в скобках что именно удалить, не индекс
# print(a)
# a.discard(3) # удаление элемента, только без генерации исключения
# print(a)
# a.pop()# удаление первого элемента,
# # генерация исключения при попытке удаления пустого множества
# print(a)
# a.clear()
# print(a) #очистка множества


# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# # # c = a.union(b)
# # # c = a | b
# # a|=b
# # c = a&b
# # c = b - a
# c = a ^ b
# a ^= b
# # print(c)
# # print(a)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# # s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# s = s1.union(s2, s3, s4, s5, s6, s7)
# print(s)
# print(len(s))
# print("Max =", max(s))
# print("Min =", min(s))

# s1 = "Hello"
# s2 = "How are you"
# s = set(s1) & set(s2)
# print(s)
# for i in s:
#     print(i, end=" ")

# s1 = 'Python'
# s2 = 'Programming language'
# s = set(s1)-set(s2)
# print(s)
# for i in s:
#     print(i, end=" ")


# frozenset

# s = frozenset([1, 2, 3, 4, 5])
# print(s)
# print(type(s))

#  Словарь (dict)

# s = [1, 2]
# d = {'one': 1, 'two': 2}
# print(s[0], s[1])
# print(d['one'], d['two'])

# s = [1, 2]
# d = {'one': 1, 'two': 2, "ten": 10}
# print(d)

# d = {"one": "один", "two": "два"}
# print(d)
# # print(type(d))
# # d["one"] = "один"
# # d["two"] = "два"
# # print(d)
#
# d1 = dict(one="один", two="два")
# print(d1)


# d = {0: "text1", "one": 45, (1, 2.3): 'кортеж', 42: [2, 3, 6, 7], True: 1}
# print(d)
# d['one'] = 100
# d[42][1] += 100*2
# print(d[42][1])

# d = {a: a for a in range(7)}
# print(d)

# d = {a: a**2 for a in range(2, 7)}
# print(d)

# d = [1, 2, 3]
# print(d)
# print(dict(d))

# users = [
#     ['igor@gmail.com', 'Igor'],
#     ['irina@gmail.com', 'Irina'],
#     ['anna@gmail.com', 'Anna'],
# ]
#
# print(users)
# d_users = dict(users)
# print(d_users)
# print()
# user = (
#     ('igor@gmail.com', 'Igor'),
#     ('irina@gmail.com', 'Irina'),
#     ('anna@gmail.com', 'Anna'),
# )
#
# print(user)
# d_user = dict(user)
# print(d_user)
#
# # print('irina@gmail.com' in d_user)
#
# for key in d_user:
#     print(d_user[key])

# d = {'one': 1, 'two': 2, 'three': 3}
# key = 'two'
#
# if key in d:
#     del d[key]
# print(d)


# d = {'one': 1, 'two': 2, 'three': 3}
# key = 'two'
#
# # if key in d:
# #     del d[key]
#
# try:
#     del d[key]
# except KeyError:
#     print("Элемента с ключем", key, "нет в словаре")
# print(d)


# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# mult = 1
# for key in d:
#     mult *= d[key]
#
# print(mult)

# d = dict()
# d[1] = input("->")
# d[2] = input("->")
# d[3] = input("->")
# d[4] = input("->")
# print(d)
# dislike = int(input("Исключить: "))
# del d[dislike]
# print(d)

# или
# d = {i: input("->") for i in range(1, 5)}
# print(d)
# dislike = int(input("Исключить: "))
# del d[dislike]
# print(d)

# d = {'one': 1, 'two': 2, 'three': 3}
# print(len(d))

# goods = {
#     "1": ["Core-i-4", 9, 4500],
#     "2": ["Core-i5-4", 3, 8500],
#     "3": ["AMD FX-6300", 6, 3700],
#     "4": ["Pentium G3220", 8, 2100],
#     "5": ["Core-i5-4350", 5, 6400]
# }
# for i in goods:
#     print(i, ")", goods[i][0], " - ", goods[i][1], " шт. по", goods[i][2], "руб", sep='')
#
# while True:
#     n = input("№: ")
#     if n != '0':
#         m = int(input("Количество: "))
#         goods[n][1] = m
#     else:
#         break
# for i in goods:
#     print(i, ")", goods[i][0], " - ", goods[i][1], " шт. по", goods[i][2], "руб", sep='')


# Методы словарей

# d = {'one': 1, 'two': 2, 'three': 3}
# print(d["two"])
# value = d.get("two")
# print(value)
# d = {'one': 1, 'two': 2, 'three': 3}
# print(d["two"])
# value = d.get("two1", "Ключа нет") #получаем элемент из словаря по заданному ключу,
# #второй параметр возвращает значение по умолчанию, если ключа нет
# print(value)
# print(d.keys()) #список ключей словаря
# print(d.items()) #список ключей и значений в виде кортежа
# print(d.values()) #список значений словаря
#
# # for i in d.keys():
# #     print(i)
# # for i in d.values():
# #     print(i)
# for key, value in d.items():
#     print(key,'=>', value)
#
# d.clear() #очистить словарь


# d = {'one': 1, 'two': 2, 'three': 3}
# d2 = d.copy() #копия словаря
# print('D=', d)
# print('D2=', d2)
#
# d["four"] = 4
# d2["five"] = 5
# print('D=', d)
# print('D2=', d2)

# d = {'one': 1, 'two': 2, 'three': 3}

# item = d.pop('two') #удаляет элемент по ключу, возращает удаляемое значение (не ключ)
# item = d.pop('two', "ключа нет")
# item = d.setdefault('four', 4) #добавляет ключ и значение по умолчанию, если ключа нет
# #если ключ есть, то значение будет игнорироваться.
# print(item)
# print(d)

# d = {'one': 1, 'two': 2, 'three': 3}
# item = d.popitem() #удаляет произвольную пару ключ и значение
# # и возвращает удаляемое значение, в виде кортежа
# print(item)
# print(d)

# d = {'one': 1, 'two': 2, 'three': 3}
# d.update({'four': 4, 'five': 5})
# print(d)

# d = {'one': 1, 'two': 2, 'three': 3}
# d.update([('four', 4), ('three', 5)])
# print(d)

# x = {"a": 1, "b": 2}
# y = {"b": 3, "c": 4}
# # z = x.copy()
# # z.update(y)
# # z = x | y #объединение словарей с сохранением в новый словарь
# z = {i: d[i] for d in [x, y] for i in d}
# print(z)

# d = {'name': "Kelly", 'age': 25, 'salary': 8000, 'city': 'New York'}
# new_d = dict()
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop('salary')
# print(d)
# print(new_d)


# sales = {
#     'John': {'№': 3056, "S": 8456, "E": 8441, "W": 2694},
#     'Tom': {'№': 34832, "S": 6786, "E": 4737, "W": 3612},
#     'Anne': {'№': 5239, "S": 4802, "E": 5820, "W": 1859},
#     'Fiona': {'№': 3904, "S": 3645, "E": 8821, "W": 2451}
#
# }
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print('\t', y, ': ', sales[x][y], sep='')
# person = input('Имя: ')
# region = input("Регион: ")
# print(sales[person][region])
# new_data = int(input("Новое значение: "))
# sales[person][region] = new_data
# print(sales[person])

# d = {'one': 1, 'two': 2, 'three': 3, "four": 4}
# new_d = {k: v for k, v in d.items() if v == 1 or v == 2}
# print(new_d)

# s = "Hello"
# d = {i: i * 3 for i in s}
# print(d)

# lt = [1, 2, 3, 4]
# # value = input("->")
# d = {i: input("->") for i in lt}
# print(d)

# d = {'one': 1, 'two': 2, 'three': 3, "four": 4}
#
# dict_one = {'name': "Igor", 'last_name': "Doe", "job": "Consultant"}
# dict_two = {'name': "Irina", 'last_name': "Smith", "job": "Manager"}
# for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
#      print(k1, v1)
#      print(k2, v2)

# pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# # print(dict(pairs))
# a, b = zip(*pairs)
# print(a)
# print(b)


# letters = ['b', 'a', 'd', 'c']
# numbers = [3, 1, 2, 4]
# data = list(zip(letters, numbers))
# print(data)
# data.sort()
# print(data)
# data1 = list(zip(numbers, letters))
# data1.sort()
# print(data1)
# data2 = dict(data1)
# print(data2)
# data3 = sorted(data2.items())
# print(data3)

# one = {'apple': 0.4, 'orange': 0.35, 'pepper': 0.5}
# two = {'pepper': 0.2, 'onion': 0.55}
#
# print({**two, **one}) #распаковка словаря
#
# for k, v in {**two, **one}.items():
#     print(k, '->', v)

# data = [2, 5, 3, 4, 1, 5]
# for i in data:
#     print(i, end=' ')
# print()
# for i in range(6):
#     print(i, end=' ')
# print()
# i = 1
# colors = ['red', 'green', 'blue']
# for color in colors:
#     print(i, ") ", color, sep='')
#     i += 1

# colors = ['red', 'green', 'blue']
# for num, val in enumerate(colors, 1):
#     print(num, ") ", val, sep='')


# n = {i: i + 1 for i in range(10, 18)}
# print(n)
#
# for i, (j, v) in enumerate(n.items(), 100):
#     print(i, ": ", j, " -> ", v, sep = '')

#
# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)


# def func(*args):
#     res = 0
#     for i in args:
#         res += i
#     return res
#
#
# print(func(2, 3, 4, 5, 1))
# print(func(2, 4, 7))
# print(func())

# def ch(*args):
#     res = []
#     sr = sum(args)/ len(args)
#     print(sr)
#
#     for num in args:
#         if num < sr:
#             res.append(num)
#     return res
#
# print(ch(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(ch(3, 6, 1, 9, 5))


# def func(a, *args):
#     return a, args
#
#
# print(func(1))
# print(func(1, 2, 3, 'abc'))

# def print_scores(student, *scores):
#     print("Student Name:", student)
#
# print_scores("Джонатан", 100, 95,88, 92, 99)
# print_scores("Роман", 96, 20, 33)

# def func(**kwargs):
#     return kwargs
#
# print(func(a=1, b=2, c=3))


# def db(**data):
#     my_dict.update(data)
#
#
# my_dict = {'one': 'first'}
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='Bob', age=31, weight=61, eyes_color="gray")
# print(my_dict)

#
# def func(aa, *args, d=0, **kwargs):
#     return aa, args, d, kwargs
#
#
# print(func('one', 5, 9, 7, 8, 1, a=1, b=2, c=3))


# Области видимости

# name = 'Tom' #Глобальная переменная
#
#
# def hi():
#     print('Hello', name)
#
#
# def bye():
#     print('Good bye', name)
#
#
# hi()
# bye()
#
# name = 'Tom' #Глобальная переменная
#
#
# def hi():
#     name = "Sam" #локальная переменная
#     surname = "Johndon"
#     print('Hello', name, surname)
#
#
# def bye():
#     print('Good bye', name)
#
#
# hi()
# bye()


# name = 'Tom' #Глобальная переменная
# surname = None
#
# def hi():
#     global name, surname
#     name = "Sam"  #локальная переменная
#     surname = "Johndon"
#     print('Hello', name, surname)
#
#
# def bye():
#     print('Good bye', name, surname)
#
# print(name)
# hi()
# bye()
# print(name)


# i = 5
#
# def func(arg = i):
#     print(arg)
#
# i = 6
# func() #5

# def add_two(a):
#     x = 2
#     return a + x
#
# print(add_two(3))


# def add_fie(a):
#     x = 2
#
#
#     def add_two(a):
#         return a + x
#
#     return add_two()
#
#
# print(add_five(3))

# import builtins
#
# name = dir(builtins)
#
# for t in name:
#     print(t)

# min1 = [5, 6, 8, 9, 7]
# print(max(min1))
# a = [5, 6, 7, 8, 8]
# print(min(a))

# def outer_func(who):
#     def inner_func():
#         print('Hello,', who)
#
#     inner_func()
#
#
# outer_func('World!')
#
# def fun1():
#     a = 6
#
#     def fun2(b):
#         a = 4
#         print("a + b =", a + b)
#
#     print('a =', a)
#     fun2(4)
#
#
# fun1()
#
# x = 25
# t = 0

# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a
#         a = 35
#         print('nonlocal: ', a)
#
#     inner()
#     t = a
#
#
# fn()
# z = x + t  # 25 + 30 = 55
# print(z)

# x = 5
#
# def fn1():
#     x = 25
#
#     def fn2():
#         x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print('fn2.x=', x)
#
#     fn2()
#     print('fn1.x=', x)
#
#
# fn1()

# Замыкания

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# add1 = outer(5)
# print(add1(10))
#
# add2 = outer(6)
# print(add2(10))
#
# print(outer(7)(10))


# def func1():
#     a = 1
#     b = "line"
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + '1'
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())

#
# def func(city):
#     s = 0
#
#     def func1():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return func1
#
#
# res1 = func('Москва')
# res1()
# res1()
#
# res2 = func('Сочи')
# res2()
# res2()
#
# res1()


# students = {
#     'Alica': 98,
#     'Bob': 67,
#     "Chris": 85,
#     'David': 75,
#     "Ella": 54,
#     "Fiona": 35,
#     'Grace': 69
# }
#
#
# def make_classifier(lower, upper):
#     def classifier_student(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return classifier_student
#
#
# A = make_classifier(80, 100)
# B = make_classifier(70, 80)
# C = make_classifier(50, 70)
# D = make_classifier(0, 50)
#
# print("A =", A(students))
# print("B =", B(students))
# print("C =", C(students))
# print("D =", D(students))


# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         pass
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj1 = func(5, 2)
# print(obj1.add())
# print(obj1.sub())
# print(obj1.mul())


# Lambda (анонимная функция)

# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)("a", 'b'))
# func = lambda x, y: x + y
# print(func(1, 2))
# print(func("a", 'b'))
#
# def summa(x, y):
#     return x + y
#
#
# print(summa(1, 2))
# print(summa("a", 'b'))


# print((lambda x, y: x**2 + y**2)(2, 5))
#
# s = lambda a=1, b=2, c=3: a + b + c
#
# print(s())
# print(s(10))
# print(s(10, 20))
# print(s(10, 20, 30))

# s = lambda *args: args
#
# print(s(1, 2, 3, 4))
# print(s(10, 20, 30))


# f = (lambda x: x*2,
#      lambda x: x*3,
#      lambda x: x*4)
#
# for i in f:
#     print(i('abc_'))


# def inc1(n):
#     def add_two(x):
#         return x + n
#
#     return add_two
#
#
# def inc(n):
#     return lambda x: x + n

# inc = (lambda n: (lambda x: x + n))
#
# print(inc(42)(1))
# print(inc(42)(3))
# f = inc(42)
# print(f(1))
# print(f(3))


# inc = (lambda n: lambda x: lambda m: n + x + m)
# print(inc(2)(4)(6))

# d = {'b': 15, 'a': 10, 'c': 4}
# lst = list(d.items())
# print(lst)
# # lst.sort(key=lambda i: i[0])
# lst.sort(key=lambda i: i[1])
# print(lst)

# def func(i):
#     return i[1]
#
# d = {'b': 15, 'a': 10, 'c': 4}
# lst = list(d.items())
# print(lst)
# # lst.sort(key=lambda i: i[0])
# lst.sort(key=func)
# print(lst)


# players = [
#     {'name': 'Антон', 'last name': "Бирюков", 'raiting': 9},
#     {'name': 'Алексей', 'last name': "Бодня", 'raiting': 10},
#     {'name': 'Федор', 'last name': "Сидоров", 'raiting': 4},
#     {'name': 'Михаил', 'last name': "Семенов", 'raiting': 6}
# ]
#
# res = sorted(players, key = lambda item: item['last name'])
# print(res)
# res = sorted(players, key = lambda item: item['raiting'])
# print(res)
# res = sorted(players, key = lambda item: item['raiting'], reverse=True)
# print(res)

# a = [(lambda x, y: x + y), (lambda x, y: x * y), (lambda x, y: x / y)]
# # b = a[0](15, 5)
# # b = a[1](15, 5)
# b = a[2](15, 5)
# print(b)

# a = {'one': lambda x: x - 1, 'two': lambda x: x + 3, 'three': lambda x: x}
# b = [-3, 10, 0, 2]
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))


# d = {
#     1: lambda: print('Понедельник'),
#     2: lambda: print('Вторник'),
#     3: lambda: print('Среда'),
#     4: lambda: print('Четверг'),
#     5: lambda: print('Пятница'),
#     6: lambda: print('Суббота'),
#     7: lambda: print('Воскресенье')
# }
# d[4]()

# print((lambda a, b: max(a, b))(15, 13))
# print((lambda a, b: a if a > b else b)(15, 13))


# print((lambda a, b, c: min(a, b, c))(9, 8, 5))

# print((lambda a, b, c: a if a < b and a < c else b if b < c else c)(9, 18, 15))


# map(func, iterable)
# def mult(t):
#     return t * 2
#
#
# lst = [1, 8, 12, -5, -10]
# # lst2 = list(map(mult, lst))
# # lst2 = set(map(mult, lst))
#
# print(lst2)

# print(list(map(lambda t: t * 2, [1, 8, 12, -5, -10])))

# t = (2.88, -1.75, 100.55)
# print(tuple(map(lambda x: int(x), t)))
# print(tuple(map(int, t)))

# areas = [3.456789, 5.578945, 7.45689, 45.45678, 78.985423, 1.245678]
# print(list(map(round, areas, range(1, 7))))


# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
# print(list(map(lambda x, y: {x, y}, st, num)))
# print(list(map(lambda x, y: (x, y), st, num)))
# print(dict(map(lambda x, y: (x, y), st, num)))

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(list(map(lambda x, y: x + y, l1, l2)))

# filter(func, iterable)

# t = ('abcd', 'abc', 'cdefq', 'def', 'ghi')
# print(tuple(filter(lambda s: len(s) == 3, t)))

# b = [66, 90, 68, 59, 76, 60, 80, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 75, b))
# print(res)

# import random
#
#
# lst = [random.randint(1, 30) for _ in range(10)]
# lst_new = list(filter(lambda x: 9 < x < 21, lst))
# print(lst)
# print('[10; 20] =', lst_new)

# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10))))
# # [0,1,2,3,4,5,6,7,8,9] -> [1,3,5,7,9] -> 1**2, 3**2...
# print(m)
# m1 = [x ** 2 for x in range(10) if x % 2]
# print(m1)


# Декораторы

# def hello():
#     return 'Hello, I am func "hello"'
#
#
# def super_func(func):
#     print('Hello, I am func "super_func"')
#     print(func())
#
#
# super_func(hello)


# def hello():
#     return 'Hello, I am func "hello"'
#
#
# test = hello
# print(test())


# def my_decorator(func):
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#
#     return func_wrapper()
#
#
# def func_test():
#     print('Hello, I am func "func_test"')


# test = my_decorator(func_test)
# test()


# def my_decoraror(func):
#     def func_wrapper():
#         print('Code before')
#         func()
#         print('Code after')
#
#     return func_wrapper
#
#
# @my_decoraror
# def func_test():
#     print('Hello, I am func "func_test"')
#
#
# func_test()


# def bold(fn):
#     def wrap():
#         return '<b>' + fn() + "</b>"
#
#     return wrap


# def italic(fn):
#     def wrap():
#         return '<i>' + fn() + "</i>"
#
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return "text"
#
#
# print(hello())

# def cnt(fn):
#     count = 0 #1
#
#     def wrap():
#         nonlocal count
#         count = count + 1
#         fn()
#         print("Вызов функции:", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("hello")
#
#
# hello()
# hello()
# hello()


# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print('Данные:', arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name('Ирина', 'Ветрова')


# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print('args:', args)
#         print('kwargs', kwargs)
#         # print('1)', args[0])
#         # print('kw)', kwargs['study'])
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, '\n')
#
#
# print_full_name('Ирина', 'Елизавета', 'Светлана', study="JavaScript")
# print_full_name('Владимир', 'Екатерина', 'Виктор')

#
# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, '= ', end='')
#             fn(x, y)
#
#         return wrap
#
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor('Разность:', "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)


# def multiply(n1):
#     def mult(fn):
#         def wrap(n2):
#             return n1 * fn(n2)
#
#         return wrap
#     return mult
# @multiply(3)
# def return_num(num):
#     return num
#
# print(return_num(5))

# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError('Не корректный тип данных')
#             for k in kwargs:
#                 return fn(*f_args, **f_kwargs):
#                 if type(f_kwargs[k]) != f_kwargs[k]):
#                     raise TypeError('Не корректный тип данных')
#
#     return wrap
#
#
# return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z="Hello! "):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, "Dog"))
# print(typed_fn2('Hello ', 'World', '!'))
# # print(typed_fn2(3, 4, 5))
# print(typed_fn3('Hello ', 'World', z=5))


# def args_decorator(tx=None, decorator_text=''):
#     def my_decorator(func):
#         def wrap(*args):
#             print(decorator_text, end='')
#             func(*args)
#
#         return wrap
#
#     if tx is None:
#         return my_decorator
#     else:
#         return my_decorator(tx)
#
#
# @args_decorator
# def hello_world(text):
#     print(text)
#
#
# @args_decorator(decorator_text="hello, ")
# def hello_world2(text):
#     print(text)
#


# def decor(args1, args2, args3, args4):
#     def args_dec(fn):
#         def wrap(x, y, w, z):
#             print(args1, x, args2, y, args3, w, args4, z, '= ', end='')
#             fn(x, y, w, z)
#
#         return wrap
#
#     return args_dec
#
#
# @decor("Сумма чисел:", '+', '+', '+')
# def summa(*au):
#     print(sum(au))
#
#
# @decor('Среднее арифметическое:', '+', '+', '+')
# def avg(*ae):
#     print(sum(ae) / len(ae))
#
#
# summa(2, 3, 3, 4)
# avg(2, 3, 3, 4)
#
# hello_world('Hi!')
# hello_world2('world!')


# print(int('18'))
# print(int(18.5))
# print(int('18.5'))


# print(int("100", 2))
# print(int("100", 8))
# print(int("100", 10))
# print(int("100", 16))

# print(bin(18))  #0b10010
# print(oct(18))  #0o22
# print(hex(18))  #0x12


# print(0b10010)
# print(0o22)
# print(0xFF)


#  #FF0000

# q = 'Pyt'
# w = 'hon'
# e = q + w
# print(e)
# # print(e * 3)
# #
# # print(e in "I am learn Python")
# # print(e[5::-1])
# e = e[:3] + 't' + e[4:]
# print(e)

# def changeCharToStr(s, c_old, c_new):
#     s2 = ""
#     i = 0
#     while i < len(s):
#         if s[i] == c_old:
#             s2 += c_new
#         i += 1
#     return s2
#
#
# str1 = 'Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования.'
# str2 = changeCharToStr(str1, 'N', 'P')
# print(str1)
# print(str2)

# print('Привет')
# print(u"Привет")


# print(b'a1b2c3')
# print(b'a1b2c3'[1])
# print(b'\xff\xfe\xfd')
# print(b'\xff\xfe\xfd'[1])

# name = "Дмитрий"
# age = 25
# print('Меня зовут ', name, ". Мне ", age, ' лет.', sep='')
# print('Меня зовут ' + name + ". Мне " + str(age), ' лет.', sep='')
#
# print(f'Меня зовут {name}. Мне {age} лет.')

# print(f'')

# dir_name = 'my_doc'
# file_name = "file.txt"
# print(fr'home\{dir_name}\{file_name}')
# print(f'home\\{dir_name}\\{file_name}')
# print(r'home\\\{dir_name}\{file_name}')
# print('home\\' + dir_name + '\\' + file_name)


# s = """
# <dir>
#     <a href="#">content</a>
# </dir>
# """
# s1 = '''<dir>
#     <a href="#">content</a>
# </dir>'''
#
# print(s)
# print(s1)

# def square(n):
#     """Принимает число n, возвращает квардат числа n"""
#     return n ** 2
#
# print(square(5))
# print(square.__doc__)

# import math as m
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * m.pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)

# print(ord('a'))
# print(ord('#'))
# print(ord('k'))
#
# while True:
#     n = input('->')
#     if n != '-1':
#         print(ord(n))
#     else:
#         break


# my_str = 'Test string for me'
# arr = [ord(x) for x in my_str]
# print("ASCII коды", arr)
# # meam = round((sum(arr)/len(arr))
# # arr.insert(0, meam)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое:", arr)
# # arr += [x for x in [ord(x) for x in (input('->' + " ")[:6])] if x not in arr]
# print(arr)

# if arr[-1] in arr[:-1]:
#     print('Количество последних элементов', arr.count(arr[-1]) - 1)
# arr.sort(revors=True)
# print(arr)

# print(chr(101))
# print(chr(84))
# print(chr(1085))
#
# a = 97
# b = 122
# #
# print(*(chr(x) for x in range(a, b + 1)) if a<b else(chr(x) for x in range(b, a + 1)) )
#
# print('Hello, world!')
# print('Ура, у меня получилось!')

# print('apple' == 'Apple')
# print('apple' > 'Apple')
# print(ord('a')) #97
# print(ord('A')) #65


# from random import randint
#
# SHORTEST = 7
# LONGEST = 10
# MIN_ASCII = 33
# MAX_ASCII = 126
#
#
# def random_password():
#     random_length = randint(SHORTEST, LONGEST)
#     res = ''
#     for i in range(random_length):
#         random_char = chr(randint(MIN_ASCII, MAX_ASCII))
#         res += random_char
#     return res
#
#
# print('Ваш случайный пароль:', random_password())

# print(dir(str))

# s = "Hello, WORLD! I am learning Python."
# print(s.capitalize())
# #приводит первую букву в верхний регистр, остальные в нижний
# print(s.lower()) #преобразует все символы в нижний регистр
# print(s.upper()) #преобразует все символы в верхний регистр
# print(s.swapcase()) #меняет регистр на противоположный
#
# print(s.count('h')) #подсчитывает количество вхождений в строки
# # (количество заданных символов)
# print(s.count('h', 1))
# print(s.count('o'))
# print(s.lower().count('o'))
# print(s.lower().count('o', 0, -5))
#
# print(s.find('Python')) #возвращает первый индекс, который соответствует заданной подстроке.
# # Если совпадений нет, то вернет -1
#
# print(s.find('Python', -3))
# print(s.index('Python')) #возвращает первый индекс, который соответствует заданной подстроке.
# print(s.index('Python1')) # Если совпадений нет, то вернет ошибку ValueError


# s = 'один два'
# ind = s.find(' ')
# print(ind)
# s = s[ind + 1:] + ' ' + s[:ind]
# print(s)

# s = 'ab12c59p7dq'
# digits = []
# for symbol in s:
#     if '1234567890'.find(symbol) != -1:
#         digits.append(int(symbol))
# print(digits)


# s = "Hello, WORLD! I am learning Python."
# print(s.rfind('l')) #поиск индекса с права на лево(поиск с конца)
# print(s.rindex('l'))
# print(s.find('l', 4)) #поиск индекса слева на право


# a = "Nearly all web services collect this basic information from users in their server logs. " \
#     "However, Python Tutor does not collect any personally identifiable information from its users."
#
# n = 'f'
#
# if a.count(n) == 1:
#     print(a.find(n))
# elif a.count(n) >= 2:
#     print(a.find(n), a.rfind(n))


# s = "I am learning Python, hello, WORLD"
# ind1 = s.find('h')
# print(ind1)
# ind2 = s.rfind('h')
# print(ind2)
# res = s[0:ind1] + s[ind2:]
# print(res)


# s = "hello, WORLD! I am learning Python."
#
# print(s.startswith('hello')) # с чего начинается строка
# print(s.endswith('Python')) # чем заканчивается строка
# # возвращает True или False

# print('abc123'.isalnum()) #состоит ли строка только из букв и цифр
# print('abc!123'.isalnum())
# print(''.isalnum())
#
# print('abcA'.isalpha())
# #строка состоит только из букв, в любом регистре
# print('abc123'.isalpha())
#
# print('abc!!123'.isdigit())
# print('123'.isdigit()) #строка состоит только из цифр


#
# print('py'.center(10, '-')) #выравнивание символов по центру
# print('py'.center(7, '='))

# print("     py".lstrip()) #удаляет пробельные символы слева
# print('py   '.rstrip()) #удаляет пробельные символы справа
# print('    py    '.strip()) #удаляет пробельные символы слева и справа
#
#
# print('https://www.python.prg'.lstrip('/:pths')) #удаляет встречающиеся символы в строке, с левой стороны,
# # до первго не совпвдвющенр символа
#
#
# print('py.$$$;'.rstrip(';$')) #удаляет встречающиеся символы в строке, с правой стороны,
# # до первго не совпвдвющенр символа
#
# print('https://www.python.orgw'.strip('/:pths.orgw'))
# print('https://www.python.orgw'.lstrip('/:pths').rstrip('.orgw'))

# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(str1.replace('Nython', "Python", 2)) #заменяет тип вхождения подстроки в строку

# s = '-'
# seq = ('a', 'b', 'c')
# print(s.join(seq))
# print('..'.join(['1', '99']))
# print('..'.join(['1', '2']))
#
# print(':'.join('Hello')) # обьединяет итерируемую последовательность в строку,
# # через символ разделитель


# print('Строка разделенная пробелами'.split( )) #разбивает строку символом пробел
# print('www.python.org.ru'.split('.')) # возвращает список, строковых значений,
# # разделенных (.)
# print('www.python.org.ru'.split('.', 2))
# print('1, 2, 3'.split(','))
# print('www.python.org.ru'.rsplit('.'))
# print('www.python.org.ru'.rsplit('.', 2))

# a = input('->').split()
# print(a)
# a = list(map(int, a))
# print(a)

# s = "В строке заменить пробелы звездочками"
# s = s.split()
# print(s)
# s = "*".join(s)
# print(s)


# s = input('ФИО: ').split()
# print(s)
# print(f'{s[0]} {s[1][0]}. {s[2][0]}.')


# Регулярные выражения

# import re
#
# print(dir(re))

import re

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# reg = 'я'
# print(re.findall(reg, s)) #возвращает список, содержащий все совпадения,
# с заданныи шаблоном
# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# reg = 'совпадения'
# print(re.findall(reg, s))
# print(re.search(reg, s)) #возвращает данные по соответствию первого с шаблоном
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())
#
# print(re.match(reg, s)) #поиск по заданному шаблому, только в начале строки

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# reg = 'Я ищу'
# print(re.findall(reg, s))
# print(re.search(reg, s))


# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# reg = 'я'
# print(re.split(reg, s))

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# reg = '\.'
# # print(re.split(reg, s))
# print(re.split(reg, s, 1)) #разбивает строку на список подстрок

# print(re.sub(reg, '!', s))  # поиск и замена
# print(re.sub(reg, '!', s, 1))


# print("Hello")
# import re

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 9812. [Hello]"
# reg = r'[^0-9]'
# print(re.findall(reg, s))
# print(ord("Я"))
# print(ord("а"))

# s1 = "Час в 24-часовом формате от 00 до 23. 2021-06-15T21:45. Минуты, в диапозоне от 00 до 59. 2021-06-15T01:09"
# r1 = '[0-2][0-9]:[0-5][0-9]'
# print(re.findall(r1, s1))

import re

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 98_12. [Hello]"
# reg = r'20*'
# # print(re.findall(reg, s))
# #
# # d = "Цифры: 7, +17, -42, 0013, 0.3"
# # print(re.findall(r'[+-]?[\d.]+', d))
#
#
# d = "05-03-1987 # Дата рождения"
#
# print("Дата рождения:", re.sub('#.*', '', d))
# print("Дата рождения:", re.sub('-', '.', re.sub('#.*', '', d)))

# d = "author=Пушкин А.С.; title = Евгений Онегин; price -200; year= 1831"
# # r1 = r'\w+\s*=\s*\w+\s*[\w.]*'
# r1 = r'\w+\s*=[^;]+'
# print(re.findall(r1, d))

# s1 = "12 сентября 2023 года"
# r1 = r"\d{2,4}"
# print(re.findall(r1, s1))

# s = "+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578"
# r = r"\+?7\d{10}"
# print(re.findall(r, s))


# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 98_12."
# reg = r'\w+\.$'
# print(re.findall(reg, s))
# print(re.findall(r'\w+', '12 + й'))
# print(re.findall(r'\w+', '12 + й', flags=re.ASCII))

# text = "hello world"
# print(re.findall(r'\w\+', text, re.DEBUG))
# reg = "я"
# print(re.findall(reg, s, re.IGNORECASE))

# text = """
# one
# two
# """
# print(re.findall(r"one.\w+", text))
# # print(re.findall(r"one$", text))
# # print(re.findall(r"one$", text, re.MULTILINE))
# print(re.findall(r"one.\w+", text, re.DOTALL))

# print(re.findall("""
# [\w-]+  # part
# @       # @
# [\w-]+  # part2
# """, "test@mail.ru", re.VERBOSE))

# text = """Python,
# python,
# PYTHON
# """
# reg = "(?im)^python"
# print(re.findall(reg, text))


# def validate_name(name):
#     return re.findall(r'^[\w-]{3,16}$', name)[0]
#
#
# print(validate_name('Python_master'))
# print(validate_name('Pyt'))

# s1 = "123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru"
# # reg = r'[\w.-]+@\w*\.?\w*\.?\w*'
# reg = r'[\w.-]+@[\w.-]+[\w]{2,3}'
# print(re.findall(reg, s1))

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall('<.*?>', text))
#
# # *?, +?, ?? - "ленивое соответствие" - захватывает минимально возможное число символов
# # {m,n}?, {,n}?, {m,}?
#
# s1 = "12 сентября 2023 года 568561"
# r1 = r"\d{3,}?"
# print(re.findall(r1, s1))

# t = "<p>Изображение <img alt='картинка' src='bg.jpg'> - фон страницы</p>"
# # reg = r'<img.*>'
# reg = r'<img\s+[^>]*?src\s*=\s*[^>]+>'
# print(re.findall(reg, t))


# t = "Петр, Ольга и Виталий отилично учатся"
# reg = "Петр|Ольга|Виталий"
# print(re.findall(reg, t))

# t = "int = 4, float = 4.0, double = 8.0f"
# reg = r"(int|double)\s*=\s*\d+[\w.]*"
# print(re.findall(reg, t))


# (?: ) - скобки не сохраняющие (группирующие)

# def validate_name(name):
#     return re.findall(r'^[a-z\d@_-]{6,18}$', name, re.IGNORECASE)
#
#
# print(validate_name('my-p@ssw0rd'))

# s1 = '127.0.0.1'  # 192.168.255.255
# # reg = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
# reg = r'(?:\d{1,3}.){3}\d{1,3}'
# print(re.findall(reg, s1))


# s1 = "Word2016, PS6, AI5"
# reg = r'(([a-z]+)(\d+))'
# print(re.findall(reg, s1, re.IGNORECASE)[0][0])

# s1 = "5 + 7*2 -4"
# reg = r'\s*([+*-])\s*'
# print(re.split(reg, s1))


# a = '31-08-2021'
# reg = r'^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])$'
# print(re.findall(reg, a))
# print(re.search(reg, a))


# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# reg = r'([0-9]+)\s(\D+)'
# print(re.findall(reg, s)[0])
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print(m[0])
# print(m[1])
# print(m[2])


# text = """
# Самара
# Москва
# Тверь
# Уфа
# Казань
# """
# count = 0
#
#
# def repl_find(m):
#     global count
#     count += 1
#     return f"<option value = '{count}'>{m.group(1)}</option>\n"
#
# print(re.findall(r'\s*(\w+)\s*', text))
# print(re.sub(r'\s*(\w+)\s*', repl_find, text))


# s = "<p>Изображения <img src='bg.jpg'> - фон страницы</p>"
# reg = r"<img\s+[^>]*src=(['\"])(.+)(?P=q)>"
# print(re.findall(reg, s))
#
# #(?P<name>) (?P=name)
#
# s = "Самолет прилетает 10/23/2023. Будем вас рады видеть после 10/24/2023"
# #24.10.2023
# reg = r"(\d{2})/(\d{2})/(\d{4})"
# print(re.sub(reg, r"\2.\1.\3", s))

# s = "yandex.com and yandex.ru"
# reg = r'(([a-z0-9\-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r"http://\1", s))


# Рекурсия
#
# def elevator(n):
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print('->', n)
#     elevator(n - 1)  # 5 4 3 2 1
#     print(n, end=' ')
#
#
# n1 = int(input("На каком Вы этаже: "))  # 5
# elevator(n1)


# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9])) #25


# def sum_list(lst):  # [9]
#     if len(lst) == 1:
#         print(lst, '-> lst[0]:', lst[0])
#         return lst[0] #9
#     else:
#         print(lst, '-> lst[0]:', lst[0])
#         return lst[0] + sum_list(lst[1:]) #1 + 3 + 5 + 7 +
#
#
# print(sum_list([1, 3, 5, 7, 9]))

#
# def to_str(n, base):# 7
#     convert = '0123456789ABCDEF'
#     if n < base:
#         return convert[n] # '7'
#     else:
#         return to_str(n // base, base) + convert[n % base] # '9' '6'
#
#
# print(to_str(18, 16))
# def negative(a):
#     if not a:
#         return 0
#     else:
#         count = negative(a[1:])
#         if a[0] < 0:
#             count += 1
#         return count
#
#
# lst = [-2, 3, 8, -11, -4, 6]
# print(lst)
# n = negative(lst)
# print(n)


# def validate_phone(number):
#     reg = r'^\+?7\s*\(?\d{3}\)?\s*[\d\s-]{7,9}$'
#     # return re.search(reg, number).group()
#     return re.findall(reg, number)[0]
#
#
# print(validate_phone('+7 499 456-45-78'))
# print(validate_phone('+74994564578'))
# print(validate_phone('7 (499) 456 45 78'))
# print(validate_phone('7 (499) 456-45-78'))


# names = ["Adam", ["Bob", ["Chet", "Cat"], "Bard", "Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# # print(names[0])
# # print(names[1])
# print(isinstance(names[0], str))
# print(isinstance(names[1], list))
# print(names[1][1][0])
# print(isinstance(names[1][1][0], list))
# print(len(names))
# print(names)


# def count_items(item_list):
#     count = 0
#     for item in item_list:
#         if isinstance(item, list):
#             count += count_items(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_items(names))

# def union(s):
#     if not s:
#         return s
#     if isinstance(s[0], list):
#         return union(s[0]) + union(s[1:])
#     return s[:1] + union(s[1:]) #["Adam",'Bob','Chet','Cat']
#
#
# print(union(names))

#
# def remove(text):
#     if not text:
#         return ''
#     if text[0] == '\t' or text[0] == '':
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print(remove(' Hello\tWorld! '))


# Линейный (последовательный) поиск

# def seq_search(s, item):
#     pos = 0
#     found = False
#     while pos < len(s) and not found:
#         if s[pos] == item:
#             found = True
#         else:
#             pos += 1
#     return found
#
#
# lst = [54, 26, 93, 17, 77, 31, 44, 55, 20, 65]
# lst.sort()
# print(seq_search(lst, 93))  # True
# print(seq_search(lst, 28))  # False

#
# def seq_search(s, item):
#     pos = 0
#     found = False
#     stop = False
#     while pos < len(s) and not found and not stop:
#         if s[pos] == item:
#             found = True
#         else:
#             if s[pos] > item:
#                 stop = True
#             else:
#                 pos += 1
#     return found
#
#
# lst = [54, 26, 93, 17, 77, 31, 44, 55, 20, 65]
# lst.sort()
# print(lst)
# print(seq_search(lst, 93))  # True
# print(seq_search(lst, 28))


#  Бинарный поиск
#
# def binary_search(s, item):
#     first = 0  #0
#     last = len(s) - 1  # 3
#     found = False
#
#     while first <= last and not found:
#         midpoint = (first + last) // 2 #4
#         if s[midpoint] == item:
#             found = True
#         else:
#             if item < s[midpoint]:
#                 last = midpoint - 1
#             else:
#                 first = midpoint + 1
#     return found
#
#
# lst = [17, 20, 26, 31, 44, 54, 55, 65, 77, 93]
# print(binary_search(lst, 17))
# print(binary_search(lst, 28))


# def binary_search(s, item):
#     found = False
#     last = len(s) - 1
#     first = 0
#     found = False
#
#     while first <= last and not found:
#         midpoint = (first + last) // 2
#         if s[midpoint] == item:
#             found = True
#         else:
#             if item < s[midpoint]:
#                 last = midpoint - 1
#             else:
#                 first = midpoint + 1
#     return found
#
#
# a = [randint(1, 100) for i in range(10)]
# print(a)
# a.sort()
# print(a)
# n = int(input("Введите число: "))
# if binary_search(a, n):
#     print(f'Число {n} в списке присутствует')
# else:
#     print(f'Число {n} в списке отсутствует')


# # Aлгоритмы сортировки
# "Пузырьковая сортировка"
# from random import randint
# import time
#
# def bubble(array):
#     for i in range(len(array) - 1):
#         for j in range(len(array) - i - 1):
#             if array[j] < array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#
#
# a = [randint(1, 100) for i in range(10000)]
#
# print(a)
# start = time.monotonic()
# bubble(a)
# print(a)
# res = time.monotonic() - start
# print(round(res, 3), 'sec')


# Сортировка слияние

# def merge_sort(a):
#     n = len(a)
#     if n < 2:
#         return a
#
#     left = merge_sort(a[:n // 2])
#     right = merge_sort(a[n // 2:n])
#
#     i = j = 0
#     res = []
#
#     while i < len(left) or j < len(right):
#         if not i < len(left):
#             res.append(right[j])
#             j += 1
#         elif not j < len(right):
#             res.append(left[i])
#             i += 1
#         elif left[i] < right[j]:
#             res.append(left[i])
#             i += 1
#         else:
#             res.append(right[j])
#             j += 1
#     return res
#
#
# array = [randint(1, 100) for i in range(10000)]
# # print(array)
# start = time.monotonic()
# array = merge_sort(array)
# # print(array)
# res = time.monotonic() - start
# print(round(res, 3), 'sec')


# Сортировка Шелла


# def shell_sort(s):
#     gap = len(s)
#
#     while gap > 0:
#         for val in range(gap, len(s)):
#             cur_val = s[val]
#             pos = val
#
#             while pos >= gap and s[pos - gap] > cur_val:
#                 s[pos] = s[pos - gap]
#                 pos -= gap
#                 s[pos] = cur_val
#         gap //= 2
#     return s
#
#
# a = [randint(1, 100) for i in range(10000)]
# # print(a)
# start = time.monotonic()
# shell_sort(a)
# # print(a)
# res = time.monotonic() - start
# print(round(res, 3), 'sec')

# Быстрая сортировка
# def quick_sort(a):
#     if len(a) > 1:
#         x = a[(len(a) - 1) // 2]
#         low = [i for i in a if i < x]
#         eq = [i for i in a if i == x]
#         hi = [i for i in a if i > x]
#         a = quick_sort(low) + eq + quick_sort(hi)
#     return a
#
#
# lst = [randint(1, 100) for i in range(10000)]
# # print(lst)
# start = time.monotonic()
# # lst = quick_sort(lst)
# # print(lst)
# lst.sort()
# res = time.monotonic() - start
# print(round(res, 3), 'sec')


# Работа с файлами(Файлы)

# f = open(r'C:\Users\Аленушка\Desktop\Python212\212\text1.txt')
# print(f)
# print(*f)
# print(f.mode)
# print(f.name)
# print(f.encoding)
# f.close()
# print(f.closed)


# f = open('text1.txt', 'r')
# print(f.read(3))
# print(f.read())
# f.close()


# f = open('test.txt', 'r')
# print(f.readline())
# print(f.readline(8))
# print(f.readline())
# print(f.readline())
# f.close()

# f = open('test.txt', 'r')
# print(f.readlines(16))
# print(f.readlines())
#
# f.close()

# f = open('test.txt', 'r')
# for line in f:
#     print(line)
#
# f.close()
#
#
# fail = open('test.txt')
# count_lines = len(fail.readlines())
# print(count_lines)


# f = open('xyz.txt', 'w')
# # f.write('Hello\nWorld\n')
# # lines = ['This is line 1', 'This is line 2']
# lines = [str(i ** 5) for i in range(1, 20)]
# print(lines)
# # f.writelines(lines)
# for index in lines:
#     f.write(index + "\t")
# f.close()

# f = open("text2.txt", "w")
# f.write("Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;")
# f.close()
#
# f = open("text2.txt", "r")
# read_f = f.readlines()
# print(read_f)
# for i in range(len(read_f)):
#     if read_f[i] == "изменить строку в списке;\n":
#         read_f[i] = "Hello World!\n"
# print(read_f)
# f.close()
#
# f = open("text2.txt", "w")
# f.writelines(read_f)
# f.close()

# f = open("text1.txt", "r")
# print(f.read(3))
# print(f.tell())
# print(f.seek(1))
# print(f.read())
# print(f.tell())
# f.close()

# f = open("text1.txt", "r+")
# print(f.write("I am learning Python"))
# print(f.seek(3))
# print(f.write("-new string-"))
# print(f.tell())
# f.close()


# with open('text3.txt', 'w+') as f:
#     print(f.write('0123456789\n123456789'))
#
#
# with open('text3.txt', 'r') as f:
#     for line in f:
#         print(line[:6])


# file_name = "res_1.txt"
# lst = [4.5, 2.8, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_line(lt):
#     lt = list(map(str, lt))
#     print(lt)
#     return '\t'.join(lt)
#
#
# with open(file_name, 'w') as f:
#     f.write(get_line(lst))
#
# print("Done!")

# file_name = "res_1.txt"
#
# numbers = [4.5, 2.8, 3.9, 1.0, 0.3, 4.33, 7.777]
#
#
# def get_string(l: list) -> str:
#     return '\t'.join(map(str, l))
#
#
# with open(file_name, 'r+', encoding='utf-8') as file:
#     # text = get_string(numbers)
#     # file.write(text)
#     nums = file.read()
#     print(nums)
#     nums_list = list(map(float, nums.split('\t')))
#     print(nums_list)
#     print(len(nums_list))
#     print(sum(nums_list))

# def longest_world(file):
#     with open(file, 'r') as text:
#         w = text.read().split()
#         max_length = len(max(w, key=len))
#         res = [word for word in w if len(word) == max_length]
#         if len(res) == 1:
#             return res[0]
#         return res
#
#
# file_name = "res_1.txt"
# print(longest_world(file_name))


# text = "Строка №1\nСтрока №2\nСтрока №3\nСтрока №4\nСтрока №5\nСтрока №6\nСтрока №7\nСтрока №8\nСтрока №9\nСтрока №10\n"
#
# with open('one.txt', 'w') as f:
#     f.write(text)


# read_file = 'one.txt'
# write_file = 'two.txt'
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия - ")
#         fw.write(line)


# Модуль OS (OS.PATH)

import os
import time

# import os.path

# print(os.getcwd())  # возвращает путь к текущей директории
# print(os.listdir())  # возвращает список папок и файлов, находящихся в текущей директории
# print(os.listdir("../.."))  #

# os.mkdir("folder")  # создает директорию по указанному пути
# os.makedirs("nested1/nested2/nested3")  # создает не только конечную директорию, но и промежуточные папки

# os.remove("xyz.txt")  # удаление файла

# os.rename("nested1", "test")  # переименование папок и файлов

# os.rename("text.txt", "test/text1.txt")  # все промежуточные директории должны существовать обязательно
# os.renames("text1.txt", "text/text.txt")  # создаются промежуточные директории

# os.rmdir("folder")  # удаление пустой директории


# for root, dirs, files in os.walk("test", topdown=False):  # topdown=True - сверху вниз, topdown=False - снизу вверх
#     print("Root:", root)
#     print("Sub_dirs:", dirs)
#     print("Files:", files)

# def remove_empty_dirs(root_tree):
#     print(f"Удаление пустых директорий в ветви {root_tree}")
#     print("-" * 50)
#     for root, dirs, files in os.walk(root_tree):
#         if not os.listdir(root):
#             os.rmdir(root)
#             print(f"Директория {root} удалена.")
#     print("-" * 50)
#
#
# remove_empty_dirs("test")

# os.path

# print(os.path.split(r'D:\Python212\212\test\nested2\nested3\xyz.txt')[1])  # разбивает путь на кортеж (head, tail)
# print(os.path.dirname(r'D:\Python212\212\test\nested2\nested3\xyz.txt'))  # имя директории
# print(os.path.basename(r'D:\Python212\212\test\nested2\nested3\xyz.txt'))  # имя файла

# print(os.path.join(r'D:\Python212', '212', 'test', 'xyz.txt'))  # соединяет один или несколько компонентов пути с учетом особенностей OS

# dirs = [r'Work\F1', r'Work\F2\F21']
# for d in dirs:
#     os.makedirs(d)

# files = {
#     'Work': ['w.txt'],
#     r'Work\F1': ['f11.txt', 'f12.txt', 'f13.txt'],
#     r'Work\F2\F21': ['f211.txt', 'f212.txt']
# }
#
# for d, file in files.items():
#     for f in file:
#         file_path = os.path.join(d, f)
#         # print(file_path)
#         open(file_path, 'w').close()
#
# file_with_text = [r'Work\w.txt', r'Work\F1\f12.txt', r'Work\F2\F21\f211.txt', r'Work\F2\F21\f212.txt']
#
# for file in file_with_text:
#     with open(file, 'w') as f:
#         f.write(f"some sample text for {file} file")
#
#
# def print_tree(root, topdown):
#     print(f"Обход {root} {'сверху вниз' if topdown else 'снизу вверх'}")
#     for root, dirs, fl in os.walk(root, topdown=topdown):
#         print(root)
#         print(dirs)
#         print(fl)
#     print('-' * 50)
#
#
# print_tree('Work', topdown=False)
# print_tree('Work', True)


# print(os.path.exists(r'D:\Python212\212\test\nested2\nested3\xyz1.txt'))  # возвращает True, если путь указывает на
# существующий путь в файловой системе

# path = r'D:\Python212\212\venv\Scripts\python.exe'
# k_size = os.path.getsize(path)  # размер файла
# print(k_size // 1024)
# print(os.path.getmtime(path))  # время последнего изменения файла
# print(os.path.getatime(path))  # время последнего доступа к файлу
# t = os.path.getctime(path)  # время создания файла
# print(time.strftime("%d.%m.%Y, %H:%M:%S", time.localtime(t)))


# file_path = r'test\nested2'
#
# if os.path.exists(file_path):
#     dirs, name = os.path.split(file_path)
#     atime = os.path.getmtime(file_path)
#     print(f"{name} ({dirs}) - last access time {time.strftime('%d.%m.%Y, %H:%M:%S', time.localtime(atime))}")
# else:
#     print(f"File {file_path} does not exist!")

# print(os.path.isfile(file_path))  # возвращает True, если указанный путь является файлом
# print(os.path.isdir(file_path))  # возвращает True, если указанный путь является директорией


# dir_name = r'test\nested2'
#
# obj = os.listdir(dir_name)
# print(obj)
#
# for i in obj:
#     p = os.path.join(dir_name, i)
#     # print(p)
#     if os.path.isfile(p):
#         print(f'{i} - file - {os.path.getsize(p)} bytes')
#     elif os.path.isdir(p):
#         print(f'{i} - dir')

# OOП (объектно-ориентированное программирование)

# class Point:
#     """Класс для предоставления координат точек на плоскости"""
#     x = 1
#     y = 1
#
#
# print(dir(Point))
# print(Point.__doc__)
# class Point3D:
#     pass
#
#
# class Point:
#     x = 1
#     y = 1  # 100
#
#
# p1 = Point()
# p1.x = 410
# p1.y = 200
# Point.y = 100
# print(p1.x, p1.y)
# print(p1.__dict__)
# print(Point.__dict__)
# print(type(p1))
# print(isinstance(p1, Point3D))


# p2 = Point()
# print(p2.x, p2.y)
#
# print(id(Point))
# print(id(p1))
# print(id(p2))


# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#         print(self.__dict__)
#
#
# p1 = Point()
# # p1.x = 5
# # p1.y = 10
#
# p1.set_coord(5, 10)
# Point.set_coord(p1, 8, 12)
# # print(p1.__dict__)
#
# p2 = Point()
# # p2.x = 20
# # p2.y = 30
# p2.set_coord(20, 30)
# print(p2.__dict__)

# class Human:
#     name = "name"
#     birthday = "00.00.0000"
#     phone = '00-00-00'
#     country = "country"
#     city = "city"
#     address = 'street, house'
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\n"
#               f"Номер телефона: {self.phone}\nСтрана: {self.country}\n"
#               f"Город: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.city = city
#         self.country = country
#         self.address = address
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1А")
# h1.print_info()
# h1.set_name("Анна")
# print(h1.get_name())


# class Person:
#     skill = 10
#
#     # name = ""
#     # surname = ""
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         print(f"Инициализатор {self.name} {self.surname}")
#
#     def __del__(self):
#         print("Удаление экземпляра\n\n")
#
#     def print_info(self):
#         print("Данные о сотруднике:", self.name, self.surname)
#
#     def add_skill(self, k):
#         self.skill += k
#         print(f"Квалификация сотрудника: {self.name}", self.skill, "\n")
#
#
# p1 = Person("Viktor", "Reznik")
# p1.print_info()
# p1.add_skill(3)
# del p1
#
# p2 = Person("Anna", "Dolgih")
# p2.print_info()
# p2.add_skill(2)


# class Point:
#     count = 0  # 3
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#
# p1 = Point(5, 10)
# print(p1.count)
# print("count =", Point.count)
# p2 = Point(15, 20)
# print(p2.count)
# print("count =", Point.count)
# p3 = Point(23, 39)
# print(p3.count)
# print("count =", Point.count)
# print(p1.count)


# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print(f"Инициализация {self.name}")
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "выключается!")
#         Robot.k -= 1
#         if Robot.k == 0:
#             print(self.name, "был последним")
#         else:
#             print("Работающих роботов осталось:", Robot.k)
#
#     def say_hi(self):
#         print("Приветствую! Меня зовут:", self.name)
#
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# Robot.say_hi(droid1)
# print("Численность роботов:", Robot.k)
#
# droid2 = Robot('C-3PO')
# droid2.say_hi()
# print("Численность роботов:", Robot.k)
#
# print()
# del droid1
# del droid2
# print("Численность роботов:", Robot.k)

# class Point:
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):  # установить координаты
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coord(self):  # получить координаты
#         return self.__x, self.__y
#
#     def set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print(f"Координата X должны быть числом")
#
#     def get_x(self):
#         return self.__x
#
#     def set_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print(f"Координата Y должны быть числом")
#
#     def get_y(self):
#         return self.__y
#
#
# p1 = Point(5, 10)
# # print(p1.get_coord())
# # p1.set_coord(1.5, 7)
# # # p1.__x = 100
# # print(p1.get_coord())
# # print(p1.__x)
# # p1.y = 'abc'
# # print(p1.x, p1.y)
# # p1.set_x(8)
# # p1.set_y(16)
# # print(p1.get_x())
# # print(p1.get_y())
# print(p1.__dict__)
# print(p1._Point__x)
# p1._Point__x = 111
# print(p1.__dict__)


# class Point:
#     __slots__ = ["__x", "__y", "z"]
#
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#     def __check_value(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def set_coord(self, x, y):  # установить координаты
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами")
#
#     def get_coord(self):  # получить координаты
#         return self.__x, self.__y
#
#     def set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print(f"Координата X должны быть числом")
#
#     def get_x(self):
#         return self.__x
#
#     def set_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print(f"Координата Y должны быть числом")
#
#     def get_y(self):
#         return self.__y
#
#
# p1 = Point(5, 10)
# p1.z = 1
# print(p1.z)


# print(p1.__dict__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __get_x(self):
#         print("Вызов __get")
#         return self.__x
#
#     def __set_x(self, x):
#         print("Вызов __set")
#         self.__x = x
#
#     def __del_x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     # x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 100
# print(p1.x)
# del p1.x
# print(p1.__dict__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     @property
#     def x(self):
#         print("Вызов __get")
#         return self.__x
#
#     @x.setter
#     def x(self, x):
#         print("Вызов __set")
#         self.__x = x
#
#     @x.deleter
#     def x(self):
#         print("Удаление свойства")
#         del self.__x
#
#     # x = property(__get_x, __set_x, __del_x)
#
#
# p1 = Point(5, 10)
# p1.x = 100
# print(p1.x)
# del p1.x
# print(p1.__dict__)


# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print('Килограммы задаются только числами')
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#
# weight = KgToPounds(12)
# print(weight.kg, "кг => ", end="")
# print(weight.to_pounds(), "фунтов")
# weight.kg = 41
# print(weight.kg, "кг => ", end="")
# print(weight.to_pounds(), "фунтов")
# weight.kg = "abc"
# print(weight.kg, "кг => ", end="")
# print(weight.to_pounds(), "фунтов")

# class Person:
#     def __init__(self, name, old):
#         self.__name = name
#         self.__old = old
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, new_name):
#         self.__name = new_name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def old(self, new_old):
#         self.__old = new_old
#
#     @old.deleter
#     def old(self):
#         del self.__old
#
#
# p1 = Person("Irina", 26)
# print(p1.__dict__)
# p1.name = "Igor"
# print(p1.name)
# p1.old = 31
# print(p1.old)
# del p1.name
# print(p1.__dict__)


# class Point:
#     __count = 0
#
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#         Point.__count += 1
#
#     @staticmethod
#     def get_count():
#         return Point.__count
#
#     # get_count = staticmethod(get_count)
#
#
# p1 = Point()
# p2 = Point()
# p3 = Point()
# print(p1.__dict__)
# print(Point.get_count())
# print(p2.get_count())


# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))

# import math
#
#
# class Area:
#     count = 0  # 5
#
#     @staticmethod
#     def triangle_area(a, b, c):
#         p = (a + b + c) / 2
#         Area.count += 1
#         return math.sqrt(p * (p - a) * (p - b) * (p - c))
#
#     @staticmethod
#     def triangle_area2(a, h):
#         Area.count += 1
#         return 0.5 * a * h
#
#     @staticmethod
#     def square_area(a):
#         Area.count += 1
#         return a ** 2
#
#     @staticmethod
#     def rect_area(a, b):
#         Area.count += 1
#         return a * b
#
#     @staticmethod
#     def get_count():
#         return Area.count
#
#
# print(f"Площадь треугольника по формуле Герона:", Area.triangle_area(3, 4, 5))
# print(f"Площадь треугольника через основание и высоту:", Area.triangle_area2(6, 7))
# print(f"Площадь квадрата:", Area.square_area(7))
# print(f"Площадь квадрата:", Area.square_area(9))
# print(f"Площадь прямоугольника:", Area.rect_area(2, 6))
# print(f"Количество подсчетов площади: {Area.get_count()}")


# class Data:
#     def __init__(self, day, month, year):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     @classmethod
#     def from_string(cls, data_as_string):
#         day, month, year = map(int, data_as_string.split('.'))
#         return cls(day, month, year)
#
#     @staticmethod
#     def is_date_valid(data_as_string):
#         if data_as_string.count('.') == 2:
#             day, month, year = map(int, data_as_string.split('.'))
#             return day <= 31 and month <= 12 and year <= 3999
#
#     def string_to_db(self):
#         return f"{self.year}-{self.month}-{self.year}"
#
#
# dates = [
#     '30.12.2020',
#     '30-12-2020',
#     '89.12.2021',
#     '12.31.2022'
# ]
# for string_data in dates:
#     if Data.is_date_valid(string_data):
#         data = Data.from_string(string_data)
#         string_to_db = data.string_to_db()
#         print(string_to_db)
#     else:
#         print("Неправильная дата или формат строки с датой")
# string_data = '23.10.2021'
# day, month, year = map(int, string_data.split('.'))
# data = Data.from_string('23.10.2021')
# print(data.string_to_db())


# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, surname, num, percent, value=0):
#         self.surname = surname
#         self.num = num
#         self.percent = percent
#         self.value = value
#         print(f'Счет №{self.num} принадлежит {self.surname} был открыт.')
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счет №{self.num} принадлежит {self.surname} был закрыт.')
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f'Состояние счета: {usd_val} {Account.suffix_usd}')
#
#     def convert_to_eur(self):
#         usd_eur = Account.convert(self.value, Account.rate_eur)
#         print(f'Состояние счета: {usd_eur} {Account.suffix_eur}')
#
#     def print_balance(self):
#         print(f'Текущий баланс {self.value} {Account.suffix}')
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percents(self):
#         self.value = self.value + self.value * self.percent
#         print(f'Проценты были успешно начислены!')
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f'К сожалению у Вас нет {val} {Account.suffix}')
#         else:
#             self.value -= val
#             print(f'{val} {Account.suffix} было успешно снято!')
#         self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f'{val} {Account.suffix} было успешно добавлено!')
#         self.print_balance()
#
#     def print_info(self):
#         print('Информация о счете:')
#         print('-' * 20)
#         print(f'№{self.num}')
#         print(f'Владелец: {self.surname}')
#         print(f'Текущий баланс: {self.value} {Account.suffix}')
#         print(f'Проценты: {self.percent:.0%}')
#         print('-' * 20)
#
#
# acc = Account(num='12345', surname='Долгих', percent=0.03, value=1000)
# # acc.print_balance()
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# print()
# acc.edit_owner('Дюма')
# acc.print_info()
# print()
# acc.add_percents()
# print()
#
# acc.withdraw_money(100)
# print()
# acc.withdraw_money(3000)
# print()
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)
# print()

import re


class UserDate:
    def __init__(self, fio, old, ps, weight):
        self.varify_fio(fio)

        self.__fio = fio
        self.__old = old
        self.__password = ps
        self.__weight = weight

    @staticmethod
    def varify_fio(fio):
        if not isinstance(fio, str):
            raise TypeError("ФИО должно быть строкой")
        f = fio.split()
        if len(f) != 3:
            raise TypeError("Неверный формат ФИО")

        letters = ''.join(re.findall(r'[a-яё-]', fio, re.IGNORECASE))  # ['В', 'о', 'л', 'к', 'о', 'в',
        # 'И', 'г', 'о', 'р', 'ь', 'Н', 'и', 'к', 'о', 'л', 'а', 'е', 'в', 'и', 'ч']
        for s in f:
            print(s.strip(letters))
            if len(s.strip(letters)) !=0:
                raise TypeError("В ФИО можно использовать только буквы и дефис")



p1 = UserDate('Волков Игорь Николаевич', 26, '1234 567890', 80.8)
