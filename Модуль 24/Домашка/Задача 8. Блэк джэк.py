import random

class Card:
  card_title = {2: 'Двойка', 3: 'Тройка', 4: 'Четверка',  5: 'Пятерка', 6: 'Шестерка',
                7: 'Семерка', 8: 'Восьмерка', 9: 'Девятка', 10: 'Десятка', 11: 'Валет',
                12: 'Дама', 13: 'Король', 14: 'Туз'}

  card_point = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9,
                10: 10, 11: 10, 12: 10, 13: 10, 14: 11}

count_player = 0
count_bot = 0
for i in range(2):
  m = random.randint(2, 14)
  player_card = Card()
  count_player += player_card.card_point[m]
  print('Ваша карта', player_card.card_title[m])
print('У Вас', count_player, 'очков')
print()
for i in range(2):
  m = random.randint(2, 14)
  bot_card = Card()
  count_bot += bot_card.card_point[m]
  print('Карта крупье', bot_card.card_title[m])
print('У него', count_bot, 'очков')
print()

while True:
  if count_bot > 21 or count_player > 21:
    break
  answ = int(input('Взять карту(1) или остановиться(0)? '))
  if answ == 0:
    break
  else:
    i = random.randint(2, 14)
    player_card = Card()
    count_player += player_card.card_point[i]
    print('Ваша карта', player_card.card_title[i] + ', у Вас',
          count_player, 'очков')
    c = random.randint(2, 14)
    bot_card = Card()
    count_bot += bot_card.card_point[c]
    print('Карта крупье', bot_card.card_title[c] + ', у него',
          count_bot, 'очков')
    print()


if count_bot > 21 and count_bot > count_player:
  print('Вы выйграли!')

if count_player > 21 and count_player > count_bot:
  print('Вы проиграли!')

if count_bot > count_player and count_bot < 22:
  print('Выйграл компьютер!')

if count_bot < count_player and count_player < 22:
  print('Вы выйграли!')

if count_bot == count_player:
  print('Ничья!')