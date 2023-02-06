import random

first = [round(random.uniform(5,10), 2) for _ in range(20)]
second = [round(random.uniform(5,10), 2) for _ in range(20)]

winner = [(first[x] if first[x]>second[x] else second[x]) for x in range(len(first))]

print('Первая команда:', first)
print()
print('Вторая команда:', second)
print()
print('Победители:', winner)