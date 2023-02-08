text = input('Введите текст: ')

count_l = 0
count_u = 0
for sym in text:
  if sym.islower():
    count_l += 1
  elif sym.isupper():
    count_u += 1

if count_l >= count_u:
  print(text.lower())
else:
  print(text.upper())

