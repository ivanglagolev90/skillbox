n = int(input('Кол-во видеокарт: '))
n_list = []
ans = []

for num in range(n):
    print(num+1, 'видеокарта:', end = ' ')
    card = int(input())
    n_list.append(card)

maximum = n_list[1]
for i in n_list:
 if maximum < i:
   maximum = i

for i in n_list:
    if i != maximum:
       ans.append(i)
print('Старый список:', n_list)
print('Новый список:', ans)
