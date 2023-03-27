class Property:
    tax = 0

    def __init__(self, worth):
        self.worth = worth

    def nalog(self):
        self.tax_i = self.worth / self.tax


class Apartament(Property):
    tax = 1000

    def __init__(self, worth):
        super().__init__(worth)

    def nalog(self):
        super().nalog()
        print('\nНалог на квартиру:', self.tax_i)

    def constr(self):
        return self.tax_i


class Car(Property):
    tax = 200

    def __init__(self, worth):
        super().__init__(worth)

    def nalog(self):
        super().nalog()
        print('\nНалог на машину:', self.tax_i)

    def constr(self):
        return self.tax_i


class House(Property):
    tax = 500

    def __init__(self, worth):
        super().__init__(worth)

    def nalog(self):
        super().nalog()
        print('\nНалог на дом:', self.tax_i)

    def constr(self):
        return self.tax_i


kvart = Apartament(100000)
car = Car(50000)
house = House(90000)
kvart.nalog()
car.nalog()
house.nalog()

money = int(input('Сколько у Вас денег? '))

if money >= kvart.constr() + car.constr() + house.constr():
    print('Налоги оплачены!')
else:
    print('Для оплаты не хватает {} $.'
          .format(kvart.constr() + car.constr() + house.constr() - money))




