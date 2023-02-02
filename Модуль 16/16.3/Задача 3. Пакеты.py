n = int(input('Введите количество пакетов? '))
pack = []
decode = []
fail = 0


for i in range(n):
  print('\nПакет номер', i+1)
  for bit in range(4):
    print(bit+1, 'бит:', end=' ')
    num = int(input())
    pack.append(num)
  k = pack.count(-1)
  if k < 2:
    decode.extend(pack)
  else:
    fail+=1
    print('Слишком много ошибок!')
  pack = []

print('\nПолученное сообщение:', decode)
print('Кол-во ошибок в сооьщении:', decode.count(-1))
print('Кол-во потерянных пакетов:', fail)