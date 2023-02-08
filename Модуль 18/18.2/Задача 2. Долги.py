name = input('Имя: ')
num = input('Долг: ')


text = '{your_name}! {your_name}, привет! Как дела, {your_name}? ' \
       'Где мои {your_num} рублей? {your_name}!'.  format(your_name = name, your_num = num)
print(text)