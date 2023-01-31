import math
def detect (x, y, r):
  if -r <= math.sqrt(x**2 + y**2) <= r:
    print('Монетка где-то рядом!')
  else:
    print('Монетки рядом нет =(((')

x = float(input('Введите х: '))
y = float(input('Введите y: '))
r = float(input('Введите радиус: '))

print()
detect(x, y, r)0ю