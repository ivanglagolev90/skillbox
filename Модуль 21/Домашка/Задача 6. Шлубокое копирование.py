
def new(count, ans = None, lvl = 1):
    ans = []
    name = input('Имя? ')
    site = {
        'html': {
            'head': {
                'title': 'Куплю/продам {} недорого'.format(name)
            },
            'body': {
                'h2': 'У нас самая низкая цена на {}'.format(name),
                'div': 'Купить',
                'p': 'Продать'
            }
        }
    }

    ans.append(site)

    if count != 1:
        print(ans[:])
        ans.extend(new(count - 1, ans, lv l +1))
    else:

        print(ans[:])




a = int(input('Сколько? '))
new(a)
