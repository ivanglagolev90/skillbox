from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed

    @abstractmethod
    def move(self):
        print('Транспорт едет!')

    @abstractmethod
    def signal(self):
        print('Транспорт сигналит!')


class Music:
    def mus(self):
        print('Играет КИШ')


class Auto(Transport):
    def __init__(self, color, speed):
        super().__init__(color, speed)

    def move(self):
        super().move()
        print('Только по земле!')

    def signal(self):
        super().signal()


class Boat(Transport):
    def __init__(self, color, speed):
        super().__init__(color, speed)

    def move(self):
        super().move()
        print('Только по воде!')

    def signal(self):
        super().signal()


class Amfibia(Transport, Music):
    def __init__(self, color, speed):
        super().__init__(color, speed)

    def move(self):
        super().move()
        print('По земле и воде!')

    def signal(self):
        super().signal()


auto = Auto('красная', 100)
auto.move()

boat = Boat('синяя', 50)
boat.move()
boat.signal()

amfibia = Amfibia('желтая', 120)
amfibia.move()
amfibia.mus()