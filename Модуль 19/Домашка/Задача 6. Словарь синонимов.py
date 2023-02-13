n = int(input('Кол-во пар: '))
libr = dict()

for i in range(n):
    print(i + 1, 'пара: ', end='')
    cou = input().title().split('-')
    for pairs in cou:
        if pairs != cou[0]:
            libr[pairs] = cou[0]
        if pairs != cou[1]:
            libr[pairs] = cou[1]

print(libr)

while True:
    word = input('Введите слово: ').title()
    if word in libr:
        print(libr[word])
    else:
        print('Такого слова нет.')
