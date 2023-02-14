text = input('Введите строку: ')
list = []
for i, value in enumerate(text):
  if value == '~':
    list.append(i)
#print(list)
print('Ответ:', end=' ')
for i in list:
  print(i, end = ' ')

#. so~mec~od~e
