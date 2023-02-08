text = input('Текст: ').split()

max_word = 0
for i in range(len(text)):
  if len(text[i]) > len(text[max_word]):
    max_word = i

print('Самое длинное слово:', text[max_word])
print('Длина:', len(text[max_word]), 'символов')