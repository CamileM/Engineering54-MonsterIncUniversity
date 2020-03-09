from monster_class import *


class Teacher(Monster):

    def __init__(self, first_name, last_name, teacher_id):
        super().__init__(first_name, last_name)
        self.teacher_id = teacher_id # SHOULD BE PRIVATE __teacher_id


    def create_teacher(self):
        self.first_name = input('What is your First Name? \n')
        self.last_name = input('What is your Second Name? \n')

