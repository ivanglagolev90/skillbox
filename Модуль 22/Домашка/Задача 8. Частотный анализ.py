text_file = open('C:\\task\\22_8\\text.txt', 'r')
count = 0
for line in text_file:
    for i in line:
        if i.isalpha():
            count += 1
text_file.seek(0)

text_file = open('C:\\task\\22_8\\text.txt', 'r')
letter_libr = {}
for line in text_file:
    for i in line:
        if i.isalpha():
            if i.lower() not in letter_libr:
                letter_libr[i.lower()] = 0
            letter_libr[i.lower()] += round(1 / count, 3)
# print(letter_libr)
text_file.close()

sorted_letters = sorted(letter_libr.values(), reverse=True)
sorted_libr = {}
for i in sorted_letters:
    for k in letter_libr.keys():
        if letter_libr[k] == i:
            sorted_libr[k] = letter_libr[k]

new_file = open('C:\\task\\22_8\\analysis.txt', 'w')
for i in sorted_libr:
    answ = i + ' : ' + str(sorted_libr[i])
    # print(answ)
    new_file.write(answ)
    new_file.write('\n')

new_file.close()
