import random


class CountIterator:
    def __init__(self, limit):
        self.limit = limit
        self.count = 0
        self.a = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.limit:
            self.count += 1
            self.a += random.uniform(0, 1)
            return round(self.a, 2)
        else:
            raise StopIteration


my_iter = CountIterator(5)

for i_elem in my_iter:
    print(i_elem)

# print(round(random.uniform(0, 1), 2))