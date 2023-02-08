alphabet =["а","б","в","г","д","е","ё","ж","з","и","й","к","л","м","н","о","п","р","с","т","у","ф","х","ц","ч","ш","щ","ъ","ы","ь","э","ю","я"]

text = input('Введите текст: ').lower()
text_list = [i for i in text]
k = int(input('Сдвиг: '))

n = [(alphabet[(alphabet.index(_)+k) % 33] if _ != ' ' else ' ') for _ in text_list]

print('Шифровка:', ''.join(n))