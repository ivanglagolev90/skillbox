s = input('Введите текст: ')
text = list(s)

count = 0
change = ':'
change_for = ';'
for sym in text:
  if sym == change:
    text[count] = change_for
  count += 1

print('Исправленный текст:', end = ' ')
for i in text:
  print(i, end='')