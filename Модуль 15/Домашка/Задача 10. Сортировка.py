number = [1, 4, -3, 0, 10]

for i in range(len(number)):
  for id in range(i, len(number)):
    if number[id] < number[i]:
      number[id], number[i] = number[i], number[id]

print(number)