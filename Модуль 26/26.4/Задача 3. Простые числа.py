class CountIterator:
    def __init__(self, limit):
        self.limit = limit
        self.count = 1

    def __is_Prime(self, n):
        self.good = True
        for _ in range(2, self.count):
            if self.count % _ == 0:
                self.good = False
                break
        return self.good

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.limit:
            self.count += 1
            if self.count == 2:
                return 2
            else:
                if self.__is_Prime(self.count):
                    return self.count
                else:
                    return ''
        else:
            raise StopIteration


my_iter = CountIterator(50)

for i_elem in my_iter:
    if isinstance(i_elem, int):
        print(i_elem, end=' ')
