def make_list(n, num, l):
  for i in range(n):
     print('Введите число в', num, 'список: ', end='')
     number = int(input())
     l.append(number)
  print()

main = []
sec = []
make_list(3, 1, main)
make_list(7, 2, sec)

print('Первый список:', main)
print('Второй список:', sec)
print()
main.extend(sec)

for n in main:
  for i in range(main.count(n) -1):
    main.remove(n)
print(main)