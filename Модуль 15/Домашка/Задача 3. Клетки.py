n = int(input('Кол-во клеток: '))
n_list = []
ans = []

for num in range(n):
    print('Эффективность', num+1, 'клетки:', end = ' ')
    ef = int(input())
    n_list.append(ef)
for index in range(n):
    if n_list[index] < index:
        ans.append(n_list[index])
print('Неподходящие значения:', ans)