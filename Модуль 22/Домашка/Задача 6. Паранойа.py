alphabet =["a","b","c","d","e","f","g","h","i","j","k",
           "l","m","n","o","p","q","r","s","t","u","v",
           "w","x","y","z"]

open_file = open('C:\\task\\22_6\\text.txt', 'r')
k = 1
text_list = []
for i in open_file:
    i_text = i.lower()
    n = (''.join([(alphabet[(alphabet.index(_)+k) % 26]
                   if _ != '\n' else '\n') for _ in i_text])).title()
    text_list.append(n)
    k += 1

text_str = ''.join(text_list)

new_file = open('C:\\task\\22_6\\cipher_text.txt',
                'w', encoding='utf-8')
new_file.write(text_str)
new_file.close()







# n = [(alphabet[(alphabet.index(_)+k) % 33] if _ != ' ' else ' ') for _ in text_list]
#
# print('Шифровка:', ''.join(n))
