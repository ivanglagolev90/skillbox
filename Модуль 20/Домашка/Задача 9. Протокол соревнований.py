n = int(input('Сколькл участников? '))

count_list = []
name_list = []
for i in range(n):
    print(i + 1, 'участник:', end=' ')
    gamer = input('Введите результат и ник: ')
    gamer = gamer.split()
    count_list.append(gamer[0])
    name_list.append(gamer[1])
# print(count_list)
# print(name_list)
count_list = [int(i) for i in count_list]

while len(count_list) != 3:
    min_ind = count_list.index(min(count_list))
    name_list.remove(name_list[min_ind])
    count_list.remove(min(count_list))

print()
# print(count_list)
# print(name_list)

winners = dict(zip(count_list, name_list))
cou = 0
for count, name in sorted(winners.items(), reverse=True):
    cou += 1
    print(cou, 'место:', name, '(', count, ')')










