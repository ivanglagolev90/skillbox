class Person():
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def getname(self):
        return self.__name

    def getsurname(self):
        return self.__surname

    def getage(self):
        return self.__age


class Employer(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def cash(self):
        self.money = 1
        return self.money

    def __str__(self):
        return '\nРаботник: {} {}\nВозраст: {}'.format(
            self.getsurname(), self.getname(), self.getage())


class Manager(Employer):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def cash(self):
        super().cash()
        self.money = 13000
        return self.money

    def __str__(self):
        info = super().__str__() + '\nЗарплата: {}'.format(
            self.cash())
        return info


class Agent(Employer):
    def __init__(self, name, surname, age, sales):
        super().__init__(name, surname, age)
        self.sales = sales

    def cash(self):
        super().cash()
        self.money = 5000 + 0.05 * self.sales
        return self.money

    def __str__(self):
        info = super().__str__() + '\nЗарплата: {}'.format(
            self.cash())
        return info


class Worker(Employer):
    def __init__(self, name, surname, age, hours):
        super().__init__(name, surname, age)
        self.hours = hours

    def cash(self):
        super().cash()
        self.money = 100 * self.hours
        return self.money

    def __str__(self):
        info = super().__str__() + '\nЗарплата: {}'.format(
            self.cash())
        return info


man1 = Manager('Иван', 'Глаголев', 32)
print(man1)
man2 = Agent('Катя', 'Глаголева', 31, 200000)
print(man2)
man3 = Worker('Паша', 'Воронов', 33, 200)
print(man3)
man4 = Agent('Даня', 'Глаголев', 6, 300000)
print(man4)
man5 = Worker('Кирилл', 'Глаголев', 33, 300)
print(man5)



