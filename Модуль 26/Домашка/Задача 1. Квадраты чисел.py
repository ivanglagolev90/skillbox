class Kvadrat_2:
  def __init__(self, num):
    self.n = num
    self.count = 0

  def __iter__(self):
    return self

  def __next__(self):
    if self.count < self.n:
      self.count += 1
      a = self.count ** 2
      return a
    else:
      raise StopIteration



def kvadrat_3(num):
  for _ in range(1, num + 1):
    yield _ ** 2



n = int(input('Число: '))

kvadrat1 = (i ** 2 for i in range(1, n+1))
for _ in kvadrat1:
  print(_, end = ' ')

kvadrat2 = Kvadrat_2(n)
print()
for _ in kvadrat2:
  print(_, end = ' ')

print()
for _ in kvadrat_3(n):
  print(_, end = ' ')