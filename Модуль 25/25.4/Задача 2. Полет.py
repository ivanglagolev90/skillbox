class Can_fly:
    high = 0
    speed = 0

    def up(self):
        pass
    def fly(self):
        pass
    def down(self):
        self.high = 0
        self.speed = 0

    def __str__(self):
        return '\nВысота: {}\t Скорость: {}'.format(
            self.high, self.speed)

class Butterfly(Can_fly):
    def up(self):
        super().up()
        self.high += 1

    def fly(self):
        super().fly()
        self.speed += 0.5

class Racket(Can_fly):
    def up(self):
        super().up()
        self.high += 500
        self.speed += 1000

    def down(self):
        super().down()
        print('\nРакета упала на землю! Взрыв!')

    def fire(self):
        self.speed = 0
        print('\nВзрыd на высоте {}'.format(self.high))



butterfly = Butterfly()
butterfly.up()
butterfly.fly()
print(butterfly)
print()

racket = Racket()
print(racket)
racket.up()
print(racket)
racket.down()
print(racket)
racket.up()
racket.fire()








