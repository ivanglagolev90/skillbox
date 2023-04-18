from typing import Dict


class Person:
    def __init__(self, name, age, other=''):
        self.name = name
        self.age = age
        self.other = other

    def __get__(self) -> Dict:
        return {'Имя:': self.name, 'Возраст:': self.age, 'Другая информация:': self.other}


people_list = []
dad = Person('Ваня', 32, 'женат')
people_list.append(dad.__get__())
son1 = Person('Киря', 8)
people_list.append(son1.__get__())
mom = Person('Катя', 31, 'замужем')
people_list.append(mom.__get__())
son2 = Person('Даня', 6)
people_list.append(son2.__get__())

ans1 = sorted(people_list, key=lambda elem: elem['Возраст:'])
print(ans1)
ans2 = sorted(people_list, reverse=True, key=lambda elem: elem['Возраст:'])
print(ans2)
