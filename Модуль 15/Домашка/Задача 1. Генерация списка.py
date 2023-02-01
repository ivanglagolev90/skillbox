n = int(input('Введите число: '))
num_list = []
for num in range(1, n+1):
    if num % 2 != 0:
        num_list.append(num)
print(num_list)