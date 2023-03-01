import math


class Sphere:
    r = 0.6
    a = 0
    b = 0
    c = 0

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def set_radius(self, r):
        self.r = r

    def get_radius(self):
        return self.r

    def get_volume(self):
        return (4 / 3) * math.pi * self.r ** 3

    def get_square(self):
        return 4 * math.pi * self.r**2

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_center(self):
        return self.x, self.y, self.z

    def is_point_inside(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        return (self.a - self.x)**2 + (self.b - self.y)**2 + (self.c - self.z)**2 < self.r**2


s = Sphere(0, 0, 0)
print("get_radius:", s.get_radius())
print("get_volume:", s.get_volume())
print("get_square:", s.get_square())
print("get_center:", s.get_center())
print("get_square:", s.get_square())
s.is_point_inside(0, -1.5, 0)
print(f"is_point_inside{s.a, s.b, s.c}:", s.is_point_inside(0, -1.5, 0))
s.set_radius(1.6)
print(f"set_radius({s.r}):", s.get_radius())
print(f"is_point_inside{s.a, s.b, s.c}:", s.is_point_inside(0, -1.5, 0))

