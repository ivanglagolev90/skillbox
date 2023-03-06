site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def finder(dic, text, d, l):
    if l == True:
        if d == 0:
            return None
        else:
            if text in dic:
                return dic[text]
            else:
                for i in dic.values():
                    if isinstance(i, dict):
                        result = finder(i, text, d - 1, l)
                        if result:
                            break

    else:
        result = None

    return result


string = input('Что ищем? ')
answer = input("Хотите ввести максимальную глубину? Y/N: ").lower()
if answer == "y":
    search_depth = int(input('Введите глубину поиска: '))
    answer = True
    print(finder(site, string, search_depth, answer))
if answer == "n":
    search_depth = 3
    answer = True
    print(finder(site, string, search_depth, answer))