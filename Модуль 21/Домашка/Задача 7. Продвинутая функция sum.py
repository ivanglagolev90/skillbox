# def new(al, newl=None):
#     newl = []
#     for i in al:
#         if type(i) == int:
#             newl.append(i)
#         else:
#             newl.extend(new(i))
#     return newl
#
#
# a = [1, 2, [3, 1], [5, 1]]
# print(sum(new(a)))

def new(al):
    newl = 0
    for i in al:
        if type(i) == int:
            newl += i
        else:
            newl += new(i)
    return newl


a = [1, 2, [3, 1], [5, 1]]
print(new(a))