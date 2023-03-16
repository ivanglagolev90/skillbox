def palin(text):
    libr = {}
    for sym in text:
        libr[sym] = libr.get(sym, 0) + 1


    count = 0
    for i in libr.values():
        if i % 2 != 0:
            count += 1
    return count <= 1


count_pal = 0
open_file = open('C:\\task\\Модуль 23\\23.4\\2\\text.txt', 'r', encoding='utf-8')
error_list = open('C:\\task\\Модуль 23\\23.4\\2\\errors.log', 'w', encoding='utf-8')

try:
    for word in open_file:
        if palin(word):
            count_pal += 1

        if not word.isalpha():
            error_list.write('В файле встретилось число\n')
            raise ValueError('В файле встретилось число')


except ValueError:
    print('В файле встретилось число')

print('Количество слов из которых можно сделать палиндром:', count_pal)
open_file.close()
error_list.close()

# Возможно, вы замечали, что некоторые программы не просто
# выдают ошибку и закрываются, но и записывают эту ошибку в файл.
# Таким образом проще сформировать отчёт об ошибках, а значит, программисту
# будет проще их исправить. Это называется логированием ошибок.
# Дан файл words.txt, в котором построчно записаны слова. Необходимо определить
# количество слов, из которых можно получить палиндром (привет предыдущим модулям).
# Если в строке встречается число, то программа выдаёт ошибку ValueError и
# записывает эту ошибку в файл errors.log