import random

cort1 = tuple(random.randint(0, 5) for _ in range(5))
cort2 = tuple(random.randint(-5, 0) for _ in range(5))
cort3 = cort1 + cort2

print(cort1)
print(cort2)
print(cort3)
print('Нулей в кортеже:', cort3.count(0))
