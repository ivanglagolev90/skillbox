text = input('Введите строку: ')
sym = input('Доп. символ: ')

double = [x * 2 for x in text]
text_sym = [x+sym for x in text]

print('Список удвоенных символов:', double)
print('Склейка с дополнительным символом:', text_sym)