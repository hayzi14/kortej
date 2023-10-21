from collections import namedtuple
Student = namedtuple('Student', 'name age grade city')
students = (
   Student('Данил', '18', 4.5, 'Обь'),
   Student('Дмитрий', '17', 4.5, 'Новосибирск'),
   Student('Кирилл', '17', 5, 'Новосибирск'),
   Student('Глеб', '17', 4.1, 'Новосибиркс'),
   Student('Дима', '17', 4.8, 'Чик'),
   Student('Рамзан', '45', 3.0, 'Грозный'),
   Student('Александр', '20', 3.2, 'Омск')
)
def q(students):
   p = 0

   for student in students:
       p += student.grade
   Q = p / len(students)

   f = [student.name for student in students if student.grade >= Q]
   print('Студенты ', ', '.join(f), ' в этом месяце хорошо учатся!')

q(students)
