def spisok(a):
  libr = {}
  for i in a:
    if i in libr:
      libr[i] += 1
    else:
      libr[i] = 1
  return libr


text = input('Введите текст: ').lower()
hist = spisok(text)
print()

for sym in sorted(hist.keys()):
  print(sym, '-', hist[sym])
print()

print('Максимальная частота:', max(hist.values()))



