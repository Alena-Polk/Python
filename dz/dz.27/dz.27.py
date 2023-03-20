class Point3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return self.x + other.x, self.y + other.y, self.z + other.z

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y, self.z - other.z

    def __mul__(self, other):
        return self.x * other.x, self.y * other.y, self.z * other.z

    def __truediv__(self, other):
        return self.x / other.x, self.y / other.y, self.z / other.z

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError("Ключ должен быть строкой")

        if item == "x":
            return self.x
        elif item == "y":
            return self.y
        elif item == "z":
            return self.z

        return "Неверный ключ"

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise ValueError("Ключ должен быть строкой")

        if not isinstance(value, int or float):
            raise ValueError("Значение должно быть числом")

        if key == "x":
            self.x = value

        if key == "y":
            self.y = value

        if key == "z":
            self.z = value

    def __repr__(self):
        return f"{self.x}, {self.y}, {self.z}"


p1 = Point3D(12, 15, 18)
p2 = Point3D(6, 3, 9)
print("Координаты 1-й точки:", p1)
print("Координаты 2-й точки:", p2)
p3 = p1 + p2
print("Сложение координат:", p3)
p4 = p1 - p2
print("Вычитание координат:", p4)
p5 = p1 * p2
print("Умножение:", p5)
p6 = p1 / p2
print("Деление:", p6)
if p1 == p2:
    print("Равенство координат:", True)
else:
    print("Равенство координат:", False)
print("x =", p1["x"], "x1 =", p2["x"])
print("y =", p1["y"], "y1 =", p2["y"])
print("z =", p1["z"], "z1 =", p2["z"])
p1["x"] = 20
print("Запись значения в координату x:", p1["x"])
