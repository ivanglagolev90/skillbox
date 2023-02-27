def sort(c):
  for i in c:
    isint = isinstance(i, int)
    if not isint:
      return c
  c = tuple(sorted(c))
  return c


cort = (4, 6, 7, 3, 1, 2)
print(sort(cort))

