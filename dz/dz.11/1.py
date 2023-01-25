a1 = 2
b1 = 4
c1 = 6

a2 = 5
b2 = 8
c2 = 2

a3 = 1
b3 = 6
c3 = 8

result_global = 0


def ppd_area_global(a, b, c):
    global result_global

    def rect_area(a, b):
        return a * b

    result_global = 2 * (rect_area(a, b) + rect_area(b, c) + rect_area(a, c))


print("глобальная переменная")

ppd_area_global(a1, b1, c1)
print("Результат 1 =", result_global)

ppd_area_global(a2, b2, c2)
print("Результат 2 =", result_global)

ppd_area_global(a3, b3, c3)
print("Результат 3 =", result_global)
