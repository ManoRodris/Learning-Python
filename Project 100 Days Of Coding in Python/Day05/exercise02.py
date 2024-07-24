scores = input().split()

student_scores = []

for n in range(0, len(scores)):
  student_scores.append(int(scores[n]))

max_student_scores = student_scores[0]

for i in student_scores:
  if i > max_student_scores:
    max_student_scores = i

print(max_student_scores)


