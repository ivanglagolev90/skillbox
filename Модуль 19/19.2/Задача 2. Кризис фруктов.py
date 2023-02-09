incomes = {
    'apple': 5600.20,
    'orange': 3500.45,
    'banana': 5000.00,
    'bergamot': 3700.56,
    'durian': 5987.23,
    'grapefruit': 300.40,
    'peach': 10000.50,
    'pear': 1020.00,
    'persimmon': 310.00,
}

sum = 0
k = ''
m = min(incomes.values())
print(m)
for i in incomes.keys():
    sum += incomes[i]
    if incomes[i] == m:
        k = i

print('Общий доход за год составил', sum, 'рублей.')
print()

print('Самый маленький доход у', k, '. Он составляет', m, 'рублей')
print()

incomes.pop(k)
print('Итоговый словарь:', incomes)


