text = input('Введите текст: ')
i = 0
count = 1
out = []

while i < (len(text) - 1):
    if text[i] == text[i + 1]:
        count += 1
    else:
        out.append(text[i])
        out.append(str(count))
        count = 1
    i += 1

print('Шифровка:', ''.join(out) + text[i] + str(count))



