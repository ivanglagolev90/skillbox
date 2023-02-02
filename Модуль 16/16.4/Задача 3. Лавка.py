goods = [["яблоки", 50], ["апельсины", 190], ["груши", 100], ["нектарины", 200], ["бананы", 77]]
new_fruit = []
fruit_name = input('Новый фрукт: ')
price = int(input('Цена: '))

new_fruit.append(fruit_name)
new_fruit.append(price)
goods.append(new_fruit)
print('Новый ассортимент:', goods)

for n in goods:
    n[1] = n[1]*1.08

print('Новый ассортимент c новыми ценами:', goods)
