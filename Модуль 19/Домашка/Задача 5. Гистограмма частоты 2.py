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
print(hist)
for sym in sorted(hist.keys()):
    print(sym, '-', hist[sym])
print()

for i in set(hist.values()):
    list_ans = []
    for sym in hist.keys():
        if i == hist[sym]:
            list_ans += sym

    print(i, ':', list_ans)


