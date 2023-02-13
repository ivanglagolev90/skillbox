n = int(input('Сколько заказов? '))
libr = dict()

for i in range(n):
    print(i + 1, 'заказ: ', end='')
    cou = input().split()
    if cou[0] not in libr:
        libr[cou[0]] = cou[1:]
    else:
        libr[cou[0]] += cou[1:]

# print(libr)
libr_sort = sorted(libr)

for name in libr_sort:
    print()
    if name in libr:
        print(name.title(), ':')
        count = 0
        for piz in libr[name]:
            if count % 2 == 0:
                print()
                print(piz, end=' : ')
                count += 1
            else:
                print(piz, end='')
                count += 1

