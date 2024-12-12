from random import randint

names = ['Alex', 'Beth', 'Eleanor', 'Caroline', 'Fred', 'Dave', 'Angela']
students_score = {students: randint(1, 100) for students in names}
print(students_score)
passed_students = {students:score for students, score in students_score.items() if score >= 60}
print(passed_students)
