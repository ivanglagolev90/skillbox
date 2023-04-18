a = input('Строка: ')
print(list(filter(lambda num: num.isalpha(),
                  filter(lambda tit: tit.istitle()==False, a))))

