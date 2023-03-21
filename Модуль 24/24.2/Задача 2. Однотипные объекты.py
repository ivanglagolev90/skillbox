class Monitor:
  name = 'Samsung'
  matrix = 'VA'
  res = 'WQHD'
  freq = 0

class Headphones:
  name = 'Sony'
  sensitivity = 108
  micro = True

monitor1 = Monitor()
monitor2 = Monitor()
monitor3 = Monitor()
monitor4 = Monitor()

monitor1.freq = 60
monitor2.freq = 144
monitor3.freq = 70
monitor4.freq = 60

headphones1 = Headphones()
headphones2 = Headphones()
headphones3 = Headphones()

headphones1.micro = False

print(headphones1.micro)
print(headphones2.micro)
print(monitor2.freq)
