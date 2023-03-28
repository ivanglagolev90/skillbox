class ListLinked:
    def __init__(self):
        self.all_list = []

    def append(self, n):
        self.all_list.append(n)

    def get(self, a):
        return self.all_list[a]

    def remove(self, t):
        self.all_list.pop(t)

    def __str__(self):
        return f'{self.all_list}'


my_list = ListLinked()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)

