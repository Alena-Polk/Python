a1 = 2
b1 = 4
c1 = 6

a2 = 5
b2 = 8
c2 = 2

a3 = 1
b3 = 6
c3 = 8


def f(a, b, c):
    result_nonlocal = 0

    def ppd_area(a, b, c):
        nonlocal result_nonlocal

        def rect_area(a, b):
            return a * b

        result_nonlocal = 2 * (rect_area(a, b) + rect_area(b, c) + rect_area(a, c))

    ppd_area(a, b, c)
    print("Результат =", result_nonlocal)


print("\n\nнелокальная переменная")
f(a1, b1, c1)
f(a2, b2, c2)
f(a3, b3, c3)
