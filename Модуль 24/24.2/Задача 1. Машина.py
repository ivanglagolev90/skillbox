import random

class Toyota:
  color = 'Красный'
  cost = 1000000
  max_speed = 200
  speed = 0

car1 = Toyota()
car2 = Toyota()
car3 = Toyota()

car1.max_speed = random.randint(0, 200)
car2.max_speed = random.randint(0, 200)
car3.max_speed = random.randint(0, 200)

print(car1.max_speed)
print(car2.max_speed)
print(car3.max_speed)


