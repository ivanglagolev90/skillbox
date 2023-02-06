import random


army1 = [random.randint(50, 80) for i in range (10)]
army2 = [random.randint(30, 60) for i in range (10)]
army3 = [('Погиб' if army1[a] + army2[a] >= 100 else 'Выжил') for a in range(10)]

print('Первый отряд:', army1)
print('Второй отряд:', army2)
print('Третий отряд:', army3)