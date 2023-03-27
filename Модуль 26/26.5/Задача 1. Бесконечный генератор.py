def always():
  count = 0
  while True:
    yield count
    count += 1

for i in always():
  print(i)