def short(string, tpl):
    return min(len(string), len(tpl))


text = 'abcb'
cort = (1, 2, 3, 4, 5)

ans = ((text[i], cort[i]) for i in range(short(text, cort)))
print(ans)
for i in ans:
    print(i)


