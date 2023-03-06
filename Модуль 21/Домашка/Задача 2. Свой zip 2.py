# def my_zip(t, c):
#     length = min(len(t), len(c))
#     tpl_list = [(t[i], c[i]) for i in range(length)]
#     return tpl_list
#
#
# text = 'abcb'
# cort = (1, 2, 3, 4, 5)
#
# print(my_zip(text, cort))

def my_zip(t, c, a_list=None, i=0):
    a_list = []
    length = min(len(t), len(c))
    a_list.append((t[i], c[i]))
    if i != length - 1:
        a_list.extend(tuple(my_zip(t, c, a_list, i + 1)))
    return a_list


text = 'abcb'
cort = (1, 2, 3, 4, 5)
print(my_zip(text, cort))