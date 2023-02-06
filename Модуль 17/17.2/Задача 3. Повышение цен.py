def price(price, percent):
  return round(price * (1+percent/100), 2)

prices =[float(input('Цена: ')) for _ in range(int(input('Сколько товаров? ')))]

first = int(input('Повышение в первый год: '))
second = int(input('Повышение во второй год: '))

prices_f = [price(i, first) for i in prices]
prices_s = [price(n, second) for n in prices_f]

print('Сумма цен за каждый год:', sum(prices), ',', sum(prices_f), ',', sum(prices_s))