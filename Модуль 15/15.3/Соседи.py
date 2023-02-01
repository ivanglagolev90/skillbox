s = input('Ваедите строку: ')
text_list = list(s)
ind = int(input('Номер символа: '))

print('\nСосед слева:', text_list[ind - 2])
print('Сосед справа:', text_list[ind])

count = 0
for sym in text_list:
  if sym == text_list[ind-1]:
    count += 1

print()
if count < 2:
  print('Таких символов нет')
elif count >= 2:
  print('Таких же символов', count-1)