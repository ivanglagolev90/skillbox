import random

alphabet = ["а","б","в","г","д","е","ё","ж","з",
            "и","й","к","л","м","н","о","п","р",
            "с","т","у","ф","х","ц","ч","ш","щ",
            "ъ","ы","ь","э","ю","я"]
first = [random.choice(alphabet)
         for _ in range(10)]

second = [random.choice(alphabet)
          for _ in range(10)]

print(first)
print(second)
print()

libr1 = {}
for i, value in enumerate(first):
  libr1[i] = value 
print('Первый словарь:', libr1)
print()

libr2 = {}
for i, value in enumerate(second):
  libr2[i] = value 
print('Второй словарь:', libr2)