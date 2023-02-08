name = input('Имя: ')
num = input('Номер заказа: ')


text = 'Здравствуйте {your_name}! Ваш номер заказа {your_num}! Приятного дня!'.  format(your_name = name, your_num = num)
print(text)