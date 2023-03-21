import math

class Cicle:

    def __init__(self, x=0, y=0, r=1, index=0):
        self.x = x
        self.y = y
        self.r = r
        self.index = index

    def square(self):
        s = round(math.pi * self.r ** 2, 2)
        return s

    def perimetr(self):
        p = round(2 * math.pi * self.r)
        return p

    def plus(self, k):
        self.r *= k

    def is_intersect(self, other):
        return (self.x - other.x) ** 2 + (
                self.y - other.y) ** 2 <= (
                self.r + other.r) ** 2

    def info(self):
        print(
            'Координаты центра окружности номер {}: {}, {}\nРадиус: {}\nПлощадь окружности: {}\nПериметр окружности: {}'
            .format(
                self.index, self.x, self.y, self.r, Cicle.square(self), Cicle.perimetr(self)))


round1 = Cicle(1, 1, 2, 1)
round1.info()
print()
round2 = Cicle(6, 6, 1, 2)
round2.info()
print()
print('Окружности пересекаются:',
      round1.is_intersect(round2))
print()
round1.plus(4)
round1.info()
print()
print('Окружности пересекаются:',
      round1.is_intersect(round2))

