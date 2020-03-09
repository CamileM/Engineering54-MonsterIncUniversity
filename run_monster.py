from monster_class import *
from workshop_class import *
from student_class import *
from teacher_class import *

# ====== CLASS EXERCISE =====

# 1. As a receptionist of the University, I should be able to create a Student:

# declare a list of students
list_of_students = []
# student_id_count variable
student_id = 0

# create the while loop:
while True:
    # increment the counter
    student_id += 1
    # ask for first name
    input("What is your first name?\n")
    # ask for second name
    input('"What is your second name?\n')

    user_input = ''
    # if user input = quit,
    if user_input != 'quit':
        # quit the loop
        break

    # create students object from inputs
    list_of_students(Student)
    # add students to list
    list_of_students.append(Student)
    print(list_of_students)

# 2. As a Receptionist of the University, I should be able to create a Teacher:

# declare a list of teachers
list_of_teachers = []
# teacher_id_count variable
teacher_id = 0
# create the while loop:
while True:
    # increment the counter
    teacher_id += 1
    # ask for first name
    input("What is your first name?\n")
    # ask for second name
    input("What is your second name?\n")

    user_input = ''
    # if user input = quit,
    if user_input != 'quit':
        # quit the loop
        break
    # create teacher object from inputs
    list_of_teachers(Teacher)
    # add teacher to list
    list_of_teachers.append(Teacher)
    print(list_of_teachers)

# 3. As a Receptionist of the University, I should be able to create a workshop:

# create a list for workshops
list_of_workshop = []
# while loop
while True:

    # ask for subject
    input("What is your subject of study?\n")
    # ask for list of attendants
    list_of_students = []
    # ask for teacher name
    list_of_teachers = []
# adding workshop to list of workshops
list_of_workshop.append(Workshop)

# 4. As a Receptionist of the University, I should be able to create a Workshop:



# 5. As a Receptionist of the University, I should be able add skills to a Student Object

# create a list of skills

def super_strength_skill(Student):
    return('STRENGTH')

def shape_shifting_skill(Student):
    return('SHAPE SHIFTER')

def super_speed_skill(Student):
    return('SPEED')

def mind_control_skill(Student):
    return('TELEPATHY')

def teleportation_skill(Student):
    return('TELEPORT')

# 6. As a Receptionist of the University, I should be able to list all of the Student's Skills




# ====== CLASS EXAMPLE ======

# student1 = Student('Van', 'Helsing', 1)
# student2 = Student('Mona The', 'Vampire', 2)
# student3 = Student('The Boogey', 'Man', 3)
#
# first_name = input('Whats your first name? \n')
# last_name = input('Whats your second name? \n')
# # print(student.first_name, student.last_name)
#
# print(student1)
# print(student1.first_name, student1.last_name)
#
# print(student2)
# print(student2.first_name, student2.last_name)
#
# print(student3)
# print(student3.first_name, student3.last_name)