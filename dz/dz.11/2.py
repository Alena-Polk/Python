a1 = 2
b1 = 4
c1 = 6

a2 = 5
b2 = 8
c2 = 2

a3 = 1
b3 = 6
c3 = 8


def ppd_area_local(a, b, c):
    def rect_area(a, b):
        return a * b

    result = 2 * (rect_area(a, b) + rect_area(b, c) + rect_area(a, c))
    print("Результат =", result)


print("\n\nлокальная переменная")
ppd_area_local(a1, b1, c1)
ppd_area_local(a2, b2, c2)
ppd_area_local(a3, b3, c3)
