word = input('Ввведите слово: ')
word_list = list(word)
n = len(word_list)
flag = True

for i in range(1, n):
    if word_list[0] == word_list[n - 1] and word_list[i] == word_list[n - i - 1]:
        flag = False

if flag:
    print('Слово не палиндром')
else:
    print('Слово палиндром')