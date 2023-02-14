students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def f(dict):
    lst = []
    string = 0
    for i, values in dict.items():
        lst += (values['interests'])
        string += len(values['surname'])
    # print(lst)
    # print(string)
    return lst, string


pairs = []
for i, values in students.items():
    pairs += (i, values['age'])
# print(pairs)

print('Интересы всех студентов:', f(students)[0])
print()
print('Длина фамилий:', f(students)[1])

# Написать функцию, которая принимает в качестве аргумента словарь и возвращает два значения: полный список интересов всех студентов и общую длину всех фамилий студентов.
# Далее в основном коде вызывается функция, значения присваиваются отдельным переменным и выводятся на экран.