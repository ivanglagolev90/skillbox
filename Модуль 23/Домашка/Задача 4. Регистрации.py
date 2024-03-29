def answer(file_str):
    name, mail, age = file_str.split(" ")
    symbol = ("@", ".")
    age = int(age)
    if name.isalpha() is False:
        raise NameError("Поле «Имя» содержит НЕ только буквы")
    if age not in range(10, 100):
        raise ValueError("Поле «Имя» содержит НЕ только буквы")
    for char in symbol:
        if char not in mail:
            raise SyntaxError("Поле «Имейл» НЕ содержит @ и . (точку)")
    return file_str


with open("C:\\task\\Модуль 23\\Домашка\\4\\registrations.txt", "r", encoding="utf-8") as file, \
        open('C:\\task\\Модуль 23\\Домашка\\4\\registration_bad.log', 'a', encoding='utf-8') as error, \
        open('C:\\task\\Модуль 23\\Домашка\\4\\registrations_good.log', 'a', encoding='utf-8') as good:
    for str_in_file in file:
        print(str_in_file, end="")
        try:
            str_file = answer(str_in_file)
        except (NameError, ValueError, SyntaxError) as e:
            error.write(str_in_file + str(e) + '\n')
        else:
            good.write(str_in_file + '\n')