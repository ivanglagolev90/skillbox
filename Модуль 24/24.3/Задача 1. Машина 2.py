class Toyota:
    color = 'Красный'
    cost = 1000000
    max_speed = 200
    speed = 0

    def info(self):
        print(
            'Цвет: {}\nСтоимость: {}\nМакс. скорость: {}\nСкорость: {}\n'.format(
                self.color, self.cost, self.max_speed, self.speed))

    def input_speed(self, v):
        self.speed = v


car1 = Toyota()
car1.info()
car1.input_speed(100)
car1.info()



