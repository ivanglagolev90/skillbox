text = input('Текст: ')

a = text[:text.find('h')]
b = text[text.find('h'):text.rfind('h') + 1]
c = text[text.rfind('h') + 1:]
text = a + b[::-1] + c
print(text)
