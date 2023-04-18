class Robot:
    def __init__(self, model):
        self.model = model

    def __str__(self):
        return '\nНомер модели робота {}'.format(self.model)

    def talk(self):
        print('\nЯ робот!')


class Canfly:
    def __init__(self, model):
        self.model = model
        self.high = 0
        self.speed = 0

    def up(self, high):
        self.high = high
        print(f'\nПолнялся на {self.high} метров')

    def fly(self, speed):
        self.speed = speed
        print(f'\nЛечу, скорость: {self.speed} м/c')

    def down(self):
        self.high = 0
        self.speed = 0
        print('\nПриземлился')

    def __str__(self):
        return f'\nЯ летающий робот, модель: {self.model}/t Высота: {self.high}\t Скорость: {self.speed}'


class Mil_robot(Robot, Canfly):
    def __init__(self, model, gun):
        super().__init__(model)
        self.gun = gun

    def operate(self):
        print('\nРобот-военный (модель {}) активировал {} и защищает территорию с воздуха'.format(self.model, self.gun))


class Watch_robot(Robot, Canfly):
    def __init__(self, model):
        super().__init__(model)
        self.location = 0

    def operate(self):
        self.location += 1
        print(f'\nВеду разведку с воздуха! продвинулся на {self.location} км.')


robot = Robot('rob1')
print(robot)
robot.talk()

mil = Mil_robot('rob2', 'Пушки')
print(mil)
mil.operate()
mil.up(100)
mil.fly(200)
print(mil)
mil.down()

wat = Watch_robot('rob3')
print(wat)
wat.operate()