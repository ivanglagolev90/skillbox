def factorial(n):
  if n == 1:
    return 1
  next = factorial(n-1)
  return n*next

ans = factorial(3)
print(ans)