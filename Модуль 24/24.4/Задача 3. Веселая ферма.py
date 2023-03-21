class Potatoes:
    states = {0: 'Нет', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, i):
        self.i = i
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self):
        print('Картошка {} сейчас {}'.format(
            self.i, Potatoes.states[self.state]))


class Potatoes_line:
    def __init__(self, count):
        self.potatoes = [Potatoes(i) for i in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает!')
        for i_potatoe in self.potatoes:
            i_potatoe.grow()

    def are_all_ripe(self):
        if not all([i_potatoe.is_ripe() for i_potatoe in self.potatoes]):
            print('Картошка не дозрела\n')
        else:
            print('Вся картошка созрела')


my_garden = Potatoes_line(5)
my_garden.are_all_ripe()
for _ in range(3):
    my_garden.grow_all()
    my_garden.are_all_ripe()
