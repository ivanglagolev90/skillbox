n_workers = int(input('Сколько сотрудников? '))
work_list = []

for worker in range(n_workers):
    print('Зарплата', worker + 1, 'сотрудника: ', end='')
    cash = int(input())
    work_list.append(cash)

print()
for num in work_list:
    if num == 0:
        work_list.remove(num)

print('Осталось сотрудников:', len(work_list))
print('Зарплаты:', work_list)
print()

print('Максимальная зарплата:', max(work_list))
print('Минимальная зарплата:', min(work_list))