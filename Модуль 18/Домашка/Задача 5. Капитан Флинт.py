ox = input('По ост OX: ').split()
oy = input('По ост OY: ').split()

x = 0
y = 0

if oy[0] == 'North':
  y += int(oy[1])
elif oy[0] == 'South':
  y -= int(oy[1])
elif ox[0] == 'West':
  x -= int(ox[1])
elif ox[0] == 'East':
  x += int(ox[1])

print('Координаты:', x, y)
