from monster_class import *
from workshop_class import *
from student_class import *
from teacher_class import *

# ====== CLASS EXERCISE =====

student_id = 0
teacher_id = 0

user_input = ''

list_of_students = []

list_of_teachers = []

list_of_workshop = []

while True:

    student_id += 1
    teacher_id += 1

    print('')
    user_input = input("Press 1 for Student, Press 2 for Teacher OR Press 3 to view the Workshops: \n")
    if user_input == '1':


        print("============ ADDING A STUDENT ============")
        first_name = input("What is your first name?\n")
        last_name = input("What is your second name?\n")
        student = Student(first_name, last_name, student_id)

        ## ========== FORMATTING FOR STUDENTS =========
        i = 'GREAT!!! You Have Selected '
        ii = ' Enjoy Your Scare Workshop'

        x = 'NICE NICE!!! You Must Be An Expert In '
        xx = 'Have A Good SCAAARE!!!'

        workshop = input("Enter the workshop code you want to study: 'EEK', 'EKΘ', 'HSS', 'PNK', 'XΦA' 'AEA'\n")
        if workshop == 'EEK':
            print(f'{i} Computer Science.{ii}')

        elif workshop == 'EKΘ':
            print(f'{x}Further & Advanced Maths. {xx}')

        elif workshop == 'HSS':
            print(f'{i} Bio Medical Science. {i}')

        elif workshop == 'PNK':
            print(f'{x} Physical & Mechanical Engineering. {xx}')

        elif workshop == 'XΦA':
            print(f'{i}Medicine. {xx}')

        elif workshop == 'AEA':
            print(f'{x}Sociology & Psychology.{ii}')

        else:
            print("!!!ENTER THE CORRECT WORKSHOP CODE (PRESS '3')!!!")

        list_of_students.append(Student)
        # print(list_of_students)


    elif user_input == '2':

        print("============ ADDING A TEACHER ============")
        first_name = input("What is your first name?\n")
        last_name = input("What is your second name?\n")
        teacher = Teacher(first_name, last_name, teacher_id)

        # ========== FORMATTING FOR TEACHERS =========
        i = 'GREAT!!! You Will Be Leading '
        ii = ''

        x = ''
        xx = ''

        workshop = input("Enter the workshop code to lead: 'EEK', 'EKΘ', 'HSS', 'PNK', 'XΦA' 'AEA'\n")
        if workshop == 'EEK':
            print(f'{i} Computer Science')

        elif workshop == 'EKΘ':
            print('Further & Advanced Maths')

        elif workshop == 'HSS':
            print('Bio Medical Science')

        elif workshop == 'PNK':
            print('Physical & Mechanical Engineering')
        elif workshop == 'XΦA':
            print('Medicine')

        elif workshop == 'AEA':
            print('Sociology & Psychology')

        else: print("!!!ENTER THE CORRECT WORKSHOP CODE (PRESS '3')!!!")

        list_of_teachers.append(Teacher)
        # print(list_of_teachers)

    elif user_input == '3':

        print("==============================================================")
        print("============WORKSHOP==========||=============CODE=============")
        print('')
        print("These Are The Workshops Currently Taking Place At MonsterInc University: ")
        print('')
        print("Computer Science : EEK")
        print("Further & Advanced Maths : EKΘ")
        print("Bio Medical Science : HSS")
        print("Physical & Mechanical Engineering : PNK")
        print("Medicine : XΦA")
        print("Sociology & Psychology : AEA")
        print('')

        list_of_workshop.append(Workshop)


        # print(list_of_workshop)

        # user_input = ''
        # if user_input != 'quit':
        #     break

        # input("What is your subject of study?\n")
