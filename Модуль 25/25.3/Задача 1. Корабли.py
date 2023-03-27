class Ships:
    def __init__(self, model):
        self.model = model

    def __str__(self):
        return '\nМодель корабля {}'.format(
            self.model)

    def sail(self):
        print('\nКорабль модели {} куда-то плывет!'
              .format(self.model))


class Warship(Ships):
    def __init__(self, model, gun):
        super().__init__(model)
        #self.model = model
        self.gun = gun

    def attack(self):
        print('\nКорабль модели {} атакует с оружием {}!'
              .format(self.model, self.gun))


class Cargoship(Ships):
    def __init__(self, model):
        super().__init__(model)
        self.model = model
        self.zagruska = 0

    def load(self):
        print('\nЗагружаем корабль модели {}'
              .format(self.model))
        self.zagruska += 1
        print('Текущая закруженность корабля {}'
              .format(self.zagruska))

    def upload(self):
        if self.zagruska > 0:
            self.zagruska -= 1
            print('\nРазгружаем корабль модели {}'
                  .format(self.model))
        else:
            print('\nКорабль модели {} уже разгружен!'
                  .format(self.model))
        print('Текущая закруженность корабля {}'
              .format(self.zagruska))


war = Warship('фарк', 'суперпушки')
war.attack()

cargo = Cargoship('fnrshj')
cargo.load()
cargo.sail()
cargo.upload()
cargo.upload()
print(war)
print(cargo)




