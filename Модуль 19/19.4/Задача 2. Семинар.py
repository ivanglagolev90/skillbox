import random

nums_1 = [29, 17, 10, 15, 13, 22, 12, 22, 7, 24, 26, 3, 11, 2, 3, 16, 19, 21, 2, 3, 8, 27, 2, 17, 2, 20, 12, 21, 3, 1]
nums_2 = [16, 21, 30, 24, 5, 7, 23, 13, 11, 5, 21, 5, 19, 9, 12, 9, 15, 16, 29, 8, 16, 1, 22, 15, 16, 9, 1, 13, 21, 21]

nums_1 = set(nums_1)
nums_2 = set(nums_2)
print(nums_1)
print(nums_2)
print()
m1 = min(nums_1)
m2 = min(nums_2)
print('Минимальный элемент 1-го множества:', m1)
print('Минимальный элемент 2-го множества:', m2)
print()
nums_1.discard(m1)
nums_2.discard(m2)
ran1 = random.randint(100, 200)
ran2 = random.randint(100, 200)
print('Случайное число для 1-го множества:', ran1)
print('Случайное число для 1-го множества:', ran2)
print()
nums_1.add(ran1)
nums_2.add(ran2)
sum = nums_1.union(nums_2)
print('Объединение множеств:', sum)
print('Пересечение множеств:', nums_1&nums_2)
print('Элементы, входящие в nums_2, но не входящие в nums_1:', nums_2-nums_1)
