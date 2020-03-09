from monster_class import *


class Teacher(Monster):

    def __init__(self, teacher_id, first_name, last_name):
        self.teacher_id = teacher_id # SHOULD BE PRIVATE __teacher_id
        self.first_name = first_name
        self.last_name = last_name

    def create_teacher(self):
        self.first_name = input('What is your First Name? \n')
        self.last_name = input('What is your Second Name? \n')

