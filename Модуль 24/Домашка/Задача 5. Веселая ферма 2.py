class Potatoes:
    states = {0: 'Нет', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, i):
        self.i = i
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state(rab)

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def print_state(self, worker):
        print('Картошка {} сейчас {}'.format(self.i, Potatoes.states[self.state]))
        print('{} ухаживает за грядкой'.format(worker.name))


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


class Worker:
    def __init__(self, name):
        self.name = name

    def work_out(self, line):
        line.potatoes = []
        print(self.name, 'все собрал. Сажай заново!')


rab = Worker('Ванька')
my_garden = Potatoes_line(3)
my_garden.are_all_ripe()
for _ in range(3):
    my_garden.grow_all()
    my_garden.are_all_ripe()
print()
print('Всего картошки:',
      len(my_garden.potatoes), 'грядок')
print()
rab.work_out(my_garden)
print()
print('Всего картошки:', 
      len(my_garden.potatoes), 'грядок')

