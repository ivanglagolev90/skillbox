def factorial(n, i = 0):
  print(i)
  if i != n:
    factorial(n, i+1)

num = int(input('Число: '))
ans = factorial(num)
