class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        print("Длина прямоугольника:", self.length)
        print("Ширина прямоугольника:", self.width)

    def square_rectangle(self):
        s = self.length * self.width
        print("Площадь прямоугольника:", s)

    def rectangle_perimeter(self):
        p = 2 * (self.length + self.width)
        print("Периметр прямоугольника:", p)

    def rectangle_hypotenuse(self):
        h = (self.length ** 2 + self.width ** 2) ** 0.5
        print("Гипотенуза прямоугольника:", round(h, 2))

    def drawing(self):
        for i in range(self.length):
            for j in range(self.width):
                print('*', end='')
            print()


pr = Rectangle(3, 9)
pr.square_rectangle()
pr.rectangle_perimeter()
pr.rectangle_hypotenuse()
pr.drawing()

