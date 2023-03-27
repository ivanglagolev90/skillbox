class Robot:
  def __init__(self, model):
    self.model = model

  def __str__(self):
    return '\nНомер модели робота {}'.format(
        self.model)

class Vac_robot(Robot):
  def __init__(self, model):
    super().__init__(model)
    self.meshok = 0

  def operate(self):
    self.meshok += 1
    print('Робот-пылесос (модель {}) пылесосит пол.\nТекущая заполняемость мешка {}'
          .format(self.model, self.meshok))

class Mil_robot(Robot):
  def __init__(self, model, gun):
    super().__init__(model)
    self.gun = gun

  def operate(self):
    print('Робот-военный (модель {}) активировал {} и защищает территорию'
          .format(self.model, self.gun))

class Wat_robot(Mil_robot):
  def __init__(self, model, gun):
    super().__init__(model, gun)
    self.depth = 0


  def operate(self):
    super().operate()
    print('\nНаблюдение под водой!')


vac = Vac_robot('sddf')
print(vac)
vac.operate()

mil = Mil_robot('wwer', 'Пушки')
print(mil)
mil.operate()

wat = Wat_robot('zxcc', 'Водные пушки')
print(wat)
wat.operate()