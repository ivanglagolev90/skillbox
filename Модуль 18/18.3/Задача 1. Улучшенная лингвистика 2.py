word_list = [input('Введите слово: ') for _ in range(3)]
print()

text_list = input('Введите текст: ').split()
print()

count = 0
for i in word_list:
  for word in text_list:
    if i == word:
      count += 1

print('Кол-во повторяющихся слов:', count)