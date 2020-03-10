from monster_class import *


class Student(Monster):

    def __init__(self,first_name, last_name, student_id):
        super().__init__(first_name, last_name)
        self.__student_id = student_id


    # ==== EACH STUDENT WILL HAVE 1 SCARE SKILL ABILITY ====