from collections import namedtuple
student = namedtuple('Student', 'name age grade city')
students = (
   student('Кирилл', '29', 4.3, 'Новосибирск'),
   student('Глеб', '17', 3.3, 'Новосибирск'),
   student('Иннокентий', '25', 4.9, 'Чик'),
   student('Мухаммед', '32', 4.5, 'Прокутка'),
   student('Иван', '21', 4.0, 'Москва'),
   student('Рудольф', '34', 3.3, 'Самара'),
   student('Владимир', '31', 3.6, 'Красноярск')
)
def a(students):
   b = 0

   for student in students:
       b += student.grade
   qwe = b / len(students)

   f = [student.name for student in students if student.grade >= qwe]
   print('Ученики ', ', '.join(f), ' в этом семестре учатся хорошо!!!!!!!!! ')

a(students)
