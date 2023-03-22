class PositiveNumber:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if value > 0 and isinstance(value, int):
            self.value = value
        else:
            raise ValueError("Значение должно быть положительным целым числом")


class Triangle:
    a = PositiveNumber(0)
    b = PositiveNumber(0)
    c = PositiveNumber(0)

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __str__(self):
        return f"Треугольник со сторонами ({self.a}, {self.b}, {self.c})"

    def check_existence(self):
        if self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
            print(f"{self} существует.")
        else:
            print(f"{self} не существует.")


t1 = Triangle(2, 5, 6)
t1.check_existence()
t2 = Triangle(5, 2, 8)
t2.check_existence()
t3 = Triangle(7, 3, 6)
t3.check_existence()
