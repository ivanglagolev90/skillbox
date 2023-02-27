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


def finder(dic, text):
    if text in dic:
        return dic[text]
    for i in dic.values():
        if isinstance(i, dict):
            result = finder(i, text)
            if result:
                break
    else:
        result = None

    return result


string = input('Что ищем? ')
find_text = finder(site, string)

if find_text:
    print(find_text)
else:
    print('Такого нет.')

