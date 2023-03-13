a_file = open('C:\\task\\zen.txt', 'r')

a_list = a_file.readlines()
print('Строк в файле:', len(a_list))

count_word = 0
count_sym = 0

for i in a_list:
    string_list = i.split()
    count_word += len(string_list)
    for word in string_list:
        count_sym += len(word)


print('Количество слов:', count_word)
print('Количество букв:', count_sym)
