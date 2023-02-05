clas1 = list(range(160, 177, 2))
clas2 = list(range(162, 181, 3))

print('Первый класс:', clas1)
print()
print('Второй класс:', clas2)

clas1.extend(clas2)

for i in range(len(clas1)):
    for id in range(i, len(clas1)):
        if clas1[id] < clas1[i]:
            clas1[id], clas1[i] = clas1[i], clas1[id]

print()
print('Вместе:', clas1)