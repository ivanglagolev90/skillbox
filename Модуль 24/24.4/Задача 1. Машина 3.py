class Toyota:

    def __init__(self, color, cost, max_speed, speed):
        self.color = color
        self.cost = cost
        self.max_speed = max_speed
        self.speed = speed

    def info(self):
        print(
            'Цвет: {}\nСтоимость: {}\nМакс. скорость: {}\nСкорость: {}\n'.format(
                self.color, self.cost, self.max_speed, self.speed))

    def input_speed(self, v):
        self.speed = v


car1 = Toyota('Красный', 1000000, 200, 0)
car1.info()
car1.input_speed(100)
car1.info()