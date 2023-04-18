
class Transport:
    def __init__(self, color, speed):
        self._color = color
        self._speed = speed


    def move(self):
        print('Транспорт едет!')

    def signal(self):
        print('Транспорт сигналит!')


    @property
    def color(self):
        return self._color

    @property
    def speed(self):
        return self._speed

    @color.setter
    def color(self, color):
        self._color = color

    @speed.setter
    def speed(self, speed):
        self._speed = speed


class Music:
    def mus(self):
        print('Играет КИШ')

class Auto(Transport):
    # def __init__(self, color, speed):
    # super().__init__(color, speed)

    def move(self):
        super().move()
        print('Только по земле!')
    def signal(self):
        super().signal()



class Boat(Transport):
    # def __init__(self, color, speed):
    # super().__init__(color, speed)

    def move(self):
        super().move()
        print('Только по воде!')
    def signal(self):
        super().signal()


class Amfibia(Transport, Music):
    # def __init__(self, color, speed):
    # super().__init__(color, speed)

    def move(self):
        super().move()
        print('По земле и воде!')
    def signal(self):
        super().signal()





auto = Auto('красная', 100)
auto.move()

print(auto.color)
auto.speed = 50
print(auto.speed)

tra = Transport('red', 50)
print(tra.color)