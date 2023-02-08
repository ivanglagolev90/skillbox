import random

n_list = [random.randint(0, 5) for _ in range(int(input('Сколько чисел в списке? ')))]
print(n_list)
print()

first = [n_list[i] for i in range(len(n_list)) if n_list[i] != 0]
second = [0 for i in range(len(n_list)) if n_list[i] == 0]
n_list = first + second
print(n_list)
print()
print(first)

