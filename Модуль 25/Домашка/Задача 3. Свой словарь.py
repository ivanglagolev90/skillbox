class My_dict():
    my = {1: 'один', 2: 'два', 3: 'три'}

    def __init__(self, key):
        self.key = key
        if self.key in My_dict.my:
            self.ans = My_dict.my[self.key]
        else:
            self.ans = 0

    def get(self):
        return self.ans


a = My_dict(3)
print(a.get())

