class Family:
  name = 'Наша семья'
  family_cash = 100000
  family_house = False

  def info(self):
    print('Семья: {}\nНакопления семьи: {}\nЕсть дом: {}\n'.format(
        self.name, self.family_cash, self.family_house))

  def work_cash(self, cash):
    self.family_cash += cash
    print('Заработано {} рублей! Всего накоплений {} рублей\n'.format(
        cash, self.family_cash))

  def house(self, cost, discount = 0):
    cost -= cost * discount / 100
    if cost > self.family_cash:
      print('На покупку дома не хватает',
            cost - self.family_cash, 'рублей\n')
    else:
      self.family_house = True
      self.family_cash -= cost
      print('Ура! Купили дом! накоплений осталось {}\n'.
            format(self.family_cash))

fam = Family()
fam.info()
fam.house(10**6)
fam.work_cash(10**6)
fam.info()
fam.house(10**6, 10)
fam.info()