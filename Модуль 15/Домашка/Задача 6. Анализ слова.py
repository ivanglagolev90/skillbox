word = input('Ввведите слово: ')
word_list = list(word)
flag = True
ans = 0

for sym in word_list:
    count = 0
    for i in word_list:
        if sym == i:
            count += 1
    if count <= 1:
        ans += 1

print('Кол-во уникальных букв:', ans)

