ski_l = []
ski = int(input('Сколько коньков? '))
for i in range(ski):
    print('Размер', i + 1, 'пары: ', end='')
    number = int(input())
    ski_l.append(number)
print()

men_l = []
men = int(input('Сколько людей? '))
for i in range(men):
    print('Размер ноги', i + 1, 'человека: ', end='')
    number = int(input())
    men_l.append(number)
print()

fi_l = []
count = 0
for i in men_l:
    for m in ski_l:
        if m >= i:
            fi_l.append(i)

for n in fi_l:
    for i in range(fi_l.count(n) - 1):
        fi_l.remove(n)

print('Наибольшее кол-во людей, которые могут взять ролики:', len(fi_l))