
import random

class Fight:
    def __init__(self, name, health = 100):
        self.name = name
        self.health = health

    def punch(self):
        self.health -= 20
        print('У игрока "{}" осталось {} здоровья!\n'.format(
            self.name, self.health))
        if self.health == 0:
            print('Игрок', self.name, 'проиграл')



fighter1 = Fight('Ванька')
fighter2 = Fight('Данька')
while True:
    if fighter1.health == 0 or fighter2 == 0:
        break
    push = random.randint(1 ,2)
    if push == 1:
        print('Ванька вмазал Даньке!')
        fighter2.punch()
    if push == 2:
        print('Данила вмазал Ваньке!')
        fighter1.punch()

