import random

class TinWoodman:
    oil = 100
    overall_wood = 0
    wood_planks = 0

    def __init__(self):
        self.tree = 0
    def main_work(self):
        print('Дровосек начинает работу!')

    def search_tree(self):
        self.tree = random.randint(1, 4)
        if self.tree == 1:
            print('\nНайдена сосна!')
        elif self.tree == 2:
            print('\nНайдена Ель!')
        elif self.tree == 3:
            print('\nНайден Кедр!')
        elif self.tree == 3:
            print('\nНайден Дуб!')
        return self.tree

    def lower_oil(self, oil_punch):
        if TinWoodman.oil - oil_punch > 0:
            TinWoodman.oil -= oil_punch
            return TinWoodman.oil
        else:
            return None

    def cut_tree(self):
        if TinWoodman.oil >= 5:
            if self.tree == 0:
                print('\nДерево не найдено, нужно поискать!')
            elif self.tree == 1:
                TinWoodman.lower_oil(self, oil_punch = 10)
                if TinWoodman.lower_oil:
                    deck = 2
                    TinWoodman.overall_wood += deck
                    TinWoodman.wood_planks += 1
                    print(f'\nДровосек срубил сосну одним ударом, собрал {deck} досок. \
                    \nМасла осталось {TinWoodman.oil} %. \nВсего досок собрано {TinWoodman.overall_wood}. \
                    \nВсего деревьев срублено {TinWoodman.wood_planks}.')
                else:
                    print('\nМасло кончилось, пора домой!')
            elif self.tree == 2:
                count = 0
                for punch in range(2):
                    TinWoodman.lower_oil(self, oil_punch = 7.5)
                    if TinWoodman.lower_oil:
                        count += 1
                        print(f'Дровосек совершил {punch+1} удар, масла осталось {TinWoodman.oil} %.')
                    else:
                        print('\nМасло кончилось, пора домой!')
                        break
                if count == 2:
                    deck = 3
                    TinWoodman.overall_wood += deck
                    TinWoodman.wood_planks += 1
                else:
                    deck = 0
                print(f'\nДровосек срубил ель, собрал {deck} досок. \
                \nМасла осталось {TinWoodman.oil} %. \
                \nВсего досок собрано {TinWoodman.overall_wood}.\
                \nВсего деревьев срублено {TinWoodman.wood_planks}.')
            elif self.tree == 3:
                count = 0
                for punch in range(3):
                    TinWoodman.lower_oil(self, oil_punch=6)
                    if TinWoodman.lower_oil:
                        count += 1
                        print(f'Дровосек совершил {punch + 1} удар, масла осталось {TinWoodman.oil} %.')
                    else:
                        print('\nМасло кончилось, пора домой!')
                        break
                if count == 3:
                    deck = 4
                    TinWoodman.overall_wood += deck
                    TinWoodman.wood_planks += 1
                else:
                    deck = 0
                print(f'\nДровосек срубил кедр, собрал {deck} досок. \
                \nМасла осталось {TinWoodman.oil} %. \
                \nВсего досок собрано {TinWoodman.overall_wood}.\
                \nВсего деревьев срублено {TinWoodman.wood_planks}.')
            elif self.tree == 4:
                count = 0
                for punch in range(5):
                    TinWoodman.lower_oil(self, oil_punch=8)
                    if TinWoodman.lower_oil:
                        count += 1
                        print(f'Дровосек совершил {punch + 1} удар, масла осталось {TinWoodman.oil} %.')
                    else:
                        print('\nМасло кончилось, пора домой!')
                        break
                if count == 5:
                    deck = 10
                    TinWoodman.overall_wood += deck
                    TinWoodman.wood_planks += 1
                else:
                    deck = 0
                print(f'\nДровосек срубил дуб, собрал {deck} досок. \
                \nМасла осталось {TinWoodman.oil} %. \
                \nВсего досок собрано {TinWoodman.overall_wood}.\
                \nСрублено деревьев срублено {TinWoodman.wood_planks}.')
            self.tree = 0
        else:
            print('Масла слишком мало, нужно заправиться.')

    def fill_oil(self):
        TinWoodman.oil = 100
        print('Заправились маслом, погнали работать дальше!')

    def stat(self):
        print(f'\nМасла осталось {TinWoodman.oil} %. \
        \nВсего досок собрано {TinWoodman.overall_wood}.\
        \nВсего деревьев срублено {TinWoodman.wood_planks}.')

    def end_work(self):
        print(f'\nРабота закончена! Пора домой! \
        \nМасла осталось {TinWoodman.oil} %. \
        \nВсего досок собрано {TinWoodman.overall_wood}.\
        \nВсего деревьев срублено {TinWoodman.wood_planks}.')



a = TinWoodman()
a.main_work()
answ = ''
while True:
    if TinWoodman.oil <= 0:
        print('\nМасло кончилось, работа окончена!')
        break
    answ = input('\nВыберите действие: \
    \n1 – поиск дерева; \
    \n2 – срубить дерево; \
    \n3 – пополнить масло; \
    \n4 – статистика; \
    \n5 – вернуться домой. \n')

    if answ == '1':
        a.search_tree()
    elif answ == '2':
        a.cut_tree()
    elif answ == '3':
        a.fill_oil()
    elif answ == '4':
        a.stat()
    elif answ == '5':
        a.end_work()
        break
    else:
        print('Ошибка ввода')

