import math


class Pair:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def get_a(self):
        return self._a

    def set_a(self, new_a):
        self._a = new_a

    def get_b(self):
        return self._b

    def set_b(self, new_b):
        self._b = new_b

    def proizv(self):
        print("Произведение:", self._a * self._b)

    def summa(self):
        print("Сумма:", self._a + self._b)


class RightTriangle(Pair):
    def __init__(self, a, b, c=0):
        super().__init__(a, b)
        self.c = c

    def hypotenuse(self):
        self.c = round(math.sqrt(self._a ** 2 + self._b ** 2), 2)
        print("Гипотенуза треугольника ABC:", self.c)

    def square(self):
        print("Площадь треугольника ABC:", self._a * self._b / 2)

    def inform(self):
        return self._a, self._b, self.c


rec = RightTriangle(5, 8)
rec.hypotenuse()
print("Прямоугольный треуголник ABC", rec.inform())
rec.square()
print()
rec.summa()
rec.proizv()
print()
num = RightTriangle(10, 20)
num.hypotenuse()
num.summa()
num.proizv()
num.square()
