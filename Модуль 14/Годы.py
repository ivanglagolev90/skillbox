a = int(input('Введите первый год: '))
b = int(input('Введите второй год: '))
count = 0
for year in range (a, b+1):
  first = year // 1000
  second = (year // 100) % 10
  third = (year % 100) // 10
  forth = year % 10
  if first == second == third or first == second == forth or first == third == forth or second == third == forth:
    print(year)