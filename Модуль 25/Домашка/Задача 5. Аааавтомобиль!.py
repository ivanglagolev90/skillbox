from math import cos, sin


class Auto:
    def __init__(self, x, y, coal):
        self.x = x
        self.y = y
        self.coal = coal

    def change_coal(self, coal):
        self.coal = coal

    def move(self, dist):
        self.x = self.x + dist * cos(self.coal)
        self.y = self.y + dist * sin(self.coal)

    def __str__(self):
        return f'\nКоординаты x: {self.x}, y: {self.y}\nУгол двидения: {self.coal} градусов'


class Bus(Auto):
    m_count = 51

    def __init__(self, x, y, coal):
        super().__init__(x, y, coal)
        self.count = 0
        self.summ = 0

    def passengers(self):
        return self.count

        # def money(self, money):
        # self.summ += money

    def enter(self, passengers):
        if self.count < self.m_count:
            print(f'\nЗашло пассажиров: {passengers}')
            self.count += passengers

        else:
            return 'Слишком много пассажиров!'

    def exit(self, passengers):
        self.count -= passengers
        print(f'\nВышло пассажиров: {passengers}')

    def move(self, dist):
        super().move(dist)
        self.summ += 10 * (self.count * dist)
        print(f'\nПроехали: {dist}, заработали: {10 * (self.count * dist)}')

    def __str__(self):
        info = super().__str__()
        return info + f'\nЧисло пассажиров: {self.count}\nЗаработано денег: {self.summ}'


car = Auto(1, 1, 30)
print(car)
car.move(3)
print(car)
car.change_coal(60)
print(car)

bus = Bus(1, 1, -30)
print(bus)
bus.enter(10)
print(bus)
bus.move(5)
print(bus)
bus.exit(5)
print(bus)
bus.move(10)
print(bus)