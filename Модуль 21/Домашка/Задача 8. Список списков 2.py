def new(al, newl=None):
    newl = []
    for i in al:
        if type(i) == int:
            newl.append(i)
        else:
            newl.extend(new(i))
    return newl


a = [1, 2, [[3, 1], [5, 1]], [6, [5, 8]]]
print(new(a))