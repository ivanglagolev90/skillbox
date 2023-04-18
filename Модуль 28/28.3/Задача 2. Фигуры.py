from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, x, y, length, width):
        self.x = x
        self.y = y
        self.length = length
        self.width = width

    @abstractmethod
    def move(self, x, y):
        self.x = x
        self.y = y


class Resizemixin:
    def resize(self, length, width):
        self.length = length
        self.width = width


class Rectangle(Figure, Resizemixin):
    def move(self, x, y):
        super().move(x, y)


class Square(Figure, Resizemixin):
    def __init__(self, x, y, size):
        super().__init__(x, y, size, size)

    def move(self, x, y):
        super().move(x, y)


sq = Square(1, 1, 1)
sq.move(2, 2)
sq.resize(3, 3)

tr = Rectangle(2, 2, 3, 4)
tr.move(2, 3)
tr.resize(1, 6)

