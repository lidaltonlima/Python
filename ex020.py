from random import shuffle

students = list()

for index in range(4):
    students.append(input('Enter the student is name: '))

shuffle(students)

print('Order of presentation:')
for student in students:
    print(f'{students.index(student) + 1}° {student}')
    
