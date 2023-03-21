class Parent:

    def __init__(self, name, age, children):
        self.name = name
        self.age = age
        self.children = children

    def info(self):
        print('Родитель:\nИмя: {}\nВозраст: {}\n'
              .format(self.name, self.age))
        print('Дети:')
        for child in self.children:
            print(child)

    def meal(self, child):
        print('{} покормила {}'
              .format(self.name, child.name))
        child.state_meal = 1

    def rest(self, child):
        print('{} успокоила {}'
              .format(self.name, child.name))
        child.state_happy = 1

class Child:
    state_meal = {0: 'голодный', 1: 'сытый'}
    state_happy = {0: 'расстроенный', 1: 'довольный'}

    def __init__(self, name, age, meal, happy):
        self.name = name
        self.age = age
        self.state_meal = meal
        self.state_happy = happy

    def info(self):
        print('Ребенок:\nИмя: {}\nВозраст: {}\nПокушал? {}\nНастроение? {}\n'
              .format(
            self.name, self.age, Child.state_meal[self.state_meal], Child.state_happy[self.state_happy]
            )
        )


mom = Parent('Катя', 31, ['Кирилл', 'Даня'])

dana = Child('Даня', 6, 0, 0)
kiril = Child('Кирилл', 8, 1, 0)

give_meal = False
give_rest = False

mom.info()
print()
dana.info()
print()
kiril.info()
print()
mom.meal(dana)
mom.rest(dana)
mom.rest(kiril)
print()
dana.info()
print()
kiril.info()

