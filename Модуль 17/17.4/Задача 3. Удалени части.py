import random

n_list = [x for x in range(random.randint(15, 20))]
print(n_list)

a = random.randint(5, 7)
b = random.randint(10, 15)
print('а =', a)
print('b =', b)
print()


print(n_list[:a] + n_list[b:])
