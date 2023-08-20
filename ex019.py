from random import choice

students = list()

for index in range(4):
    student = input('Enter the student is name: ')
    students.append(student)

print(f'The student drawn was {choice(students)}.')
