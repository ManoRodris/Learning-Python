number_of_students = int(input("Enter the number of students: "))
students_height_list = []

for i in range(number_of_students):
    students_height = int(input(f"Enter the height of student number {i + 1}: "))
    students_height_list.append(students_height)

average_students_height = round(sum(students_height_list)/number_of_students)
print("Average height rounded to the nearest whole number = " + str(average_students_height))
print(students_height_list)