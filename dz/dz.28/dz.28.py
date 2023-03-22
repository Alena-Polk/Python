import abc


class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def perimeter(self):
        pass

    @abc.abstractmethod
    def draw(self):
        pass

    @abc.abstractmethod
    def info(self):
        pass


class Square(Shape):
    def __init__(self, side, color):
        self.side = side
        self.color = color

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side

    def draw(self):
        for i in range(self.side):
            print("*" * self.side)

    def info(self):
        print("===Квадрат===")
        print(f"Сторона: {self.side}")
        print(f"Цвет: {self.color}")
        print(f"Площадь: {self.area()}")
        print(f"Периметр: {self.perimeter()}")
        self.draw()


class Rectangle(Shape):
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def draw(self):
        for i in range(self.width):
            print("*" * self.length)

    def info(self):
        print("===Прямоугольник===")
        print(f"Длина: {self.width}")
        print(f"Ширина: {self.length}")
        print(f"Цвет: {self.color}")
        print(f"Площадь: {self.area()}")
        print(f"Периметр: {self.perimeter()}")
        self.draw()


class Triangle(Shape):
    def __init__(self, side1, side2, side3, color):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.color = color

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def draw(self):
        for i in range(self.side2):
            print(' ' * (self.side2 - 1 - i) + '*' * (1 + i * 2))

    def info(self):
        print("===Треугольник===")
        print(f"Сторона 1: {self.side3}")
        print(f"Сторона 2: {self.side2}")
        print(f"Сторона 3: {self.side1}")
        print(f"Цвет: {self.color}")
        print(f"Площадь: {self.area():.2f}")
        print(f"Периметр: {self.perimeter()}")
        self.draw()


s1 = Square(3, "red")
s2 = Rectangle(7, 3, "green")
s3 = Triangle(6, 6, 11, "yellow")

s1.info()
print()
s2.info()
print()
s3.info()
