znak = {'.', ',', ';', ':', '!', '?'}
text = input('Текст: ')
count = 0
for sym in text:
  if sym in znak:
    count+=1
print(count)

