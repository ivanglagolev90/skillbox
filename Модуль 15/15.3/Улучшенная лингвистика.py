word_list = []
count = [0, 0, 0]

for i in range(3):
    print('Введите', i+1, 'слово:', end = ' ')
    word = input()
    word_list.append(word)

text = input('Введите слово: ')
while text != 'end':
    for ind in range(3):
        if word_list[ind] == text:
            count[ind] += 1
    text = input('Введите слово: ')

print('\nПодсчет слов в тексте:')
for i in range(3):
    print(word_list[i], ':', count[i])
