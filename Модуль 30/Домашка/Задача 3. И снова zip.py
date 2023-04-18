import timeit



res: float = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)

print(res)
print("-".join(str(n) for n in range(100)))
print()

res2 = timeit.timeit("''.join(str(n)+'-' for n in range(100))", number = 10000)
print(res2)

print(''.join(str(n)+'-' for n in range(100)))
print()

res3 = timeit.timeit("''.join(list(map(lambda n: str(n)+'-', list(i for i in range(100)))))", number = 10000)
print(res2)

print(''.join(list(map(lambda n: str(n)+'-', list(i for i in range(100))))))