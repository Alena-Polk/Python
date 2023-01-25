import math

a = int(input("Количество студентов: "))
studs = {}
s = 0
for i in range(a):
    name = input(str(i+1) + "-й студент (Фамилия, Имя): ")
    points = int(input("Балл: "))
    studs[name] = points
    s += points
