text = input('Текст: ')
text = sorted(set(text))
print(text)

ans = ''
for i in text:
  if '0' <= i <= '9':
    ans += i
print('Разных цифр:', ans)