import math


def func(a, b):
    side = round((2 * math.pi * a * b), 2)
    full = round((side + 2 * (math.pi * a ** 2)), 2)

    return side, full


r = int(input('Радиус: '))
h = int(input('Высота: '))
answ = func(r, h)
# print(answ)
print('Сторона:', answ[0])
print('Полная площадь:', answ[1])