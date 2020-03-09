from monster_class import *


class Student(Monster):

    def __init__(self, student_id, first_name, last_name, scare_skill):
        super.__init__(first_name, last_name, scare_skill)
        self.__student_id = student_id

    def create_student(self):
        self.first_name = input('What is your First Name? \n')
        self.last_name = input('What is your Second Name? \n')


