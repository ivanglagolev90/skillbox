class Unit:
    def __init__(self, name, hitpoints):
        self.name = name
        self.hitpoints = hitpoints
        self.damage = 0

    def hit(self, damage):
        self.damage = damage
        self.hitpoints -= self.damage
        print('\n{} получил {} урона, текущее состояние здоровья {} очков'.format(
            self.name, self.damage, self.hitpoints))

    def __str__(self):
        return '\nИмя: {}\nТекущее состояние здоровья: {} очков'.format(
            self.name, self.hitpoints)

class Soldier(Unit):
    def __init__(self, name, hitpoints):
        super().__init__(name, hitpoints)

    def hit(self, damage):
        super().hit(damage)

class Man(Unit):
    def __init__(self, name, hitpoints):
        super().__init__(name, hitpoints)

    def hit(self, damage):
        super().hit(damage*2)



soldier = Soldier('Иван', 10)
print(soldier)
soldier.hit(5)
print(soldier)
man = Man('Катя', 20)
print(man)
man.hit(3)
print(man)

