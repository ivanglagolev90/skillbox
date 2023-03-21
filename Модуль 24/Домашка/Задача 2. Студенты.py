class Student:
    def __init__(self, full_name, number_g, academ_perfom):
        self.full_name = full_name
        self.number_g = number_g
        self.academ_perfom = academ_perfom

    def average_score(self):
        return sum(self.academ_perfom) / len(self.academ_perfom)

    def __str__(self):
        result = f'{self.full_name} {self.number_g} {self.average_score()}'
        return result

        # return self.full_name


students = []

for i in range(2):
    print(f'Студент {i + 1}: ')
    full_name = input('имя: ')
    group_n = int(input('номер группы: '))
    academic_p = list(map(int, input("оценки: ").split()))
    students.append(Student(full_name, group_n, academic_p))

sort = sorted(students, key=lambda student: student.average_score())
print(*sort, sep='\n')

































# class Student:
#     students = []
#
#     def __init__(self, name, number, balls):
#         self.name = name
#         self.number = number
#         self.balls = balls
#         student_info = [self.name, self.number, self.balls]
#         Student.students.append(student_info)
#
#
# st1 = Student('Иван', '1', [3, 4, 5, 3, 5])
# st1 = Student('Катя', '2', [3, 3, 4, 3, 5])
# print(Student.students)