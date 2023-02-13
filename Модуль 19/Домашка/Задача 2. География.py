n = int(input('Сколько стран? '))
libr = dict()

for i in range(n):
    print(i + 1, 'страна: ', end='')
    cou = input().split()
    for town in cou[1:]:
        libr[town] = cou[0]

# print(libr)

for i in range(3):
    city = input('\n{} город: '.format(i + 1))
    if city in libr:
        print('Город {} расположен в стране {}.'.format(city, libr[city]))
    else:
        print('По городу {} нет данных.'.format(city))




