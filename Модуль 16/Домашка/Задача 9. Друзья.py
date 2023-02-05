n = int(input('Введите количество друзей: '))
k = int(input('Кол-во расписок: '))
print()

all = []
for i in range(n):
    all.append(0)

for i in range(k):
    print(i + 1, 'расписка')
    whom = int(input('Кому? '))
    who = int(input('Кто? '))
    cash = int(input('Сколько? '))
    all[whom - 1] -= cash
    all[who - 1] += cash
    print()

print('Баланс друзей:')
for i in range(len(all)):
    print(i + 1, ':', all[i])