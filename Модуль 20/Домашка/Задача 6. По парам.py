import random

print('Оригинальный список:', end=' ')
alist = [random.randint(0, 9) for _ in range(10)]
print(alist)
print()

new_list = list(zip(alist[::2], alist[1::2]))

print(new_list)