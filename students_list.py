student_names  = ['Ion', 'Vasile', 'Maria']
student_grades = [  8.0,     10.0,     9.5]

for index in range(len(student_names)):
    if student_grades[index] >= 9.0:
        print(f'{(index + 1):3} {student_names[index]:20} {student_grades[index]:6.2f}')