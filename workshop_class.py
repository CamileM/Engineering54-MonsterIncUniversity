from monster_class import *

class Workshop(Monster):

    def __init__(self, teacher_id, workshop):
        self.teacher_id = teacher_id # SHOULD BE PRIVATE __teacher_id
        self.workshop = workshop
        self.list_of_attendees = []

    # ==== LIST OF WORKSHOPS IN MONSTER UNIVERSITY  ====

        # Computer Science : EEK
        # Further & Advanced Maths : EKΘ
        # Bio Medical Science : HSS
        # Physical & Mechanical Engineering : PNK
        # Medicine : XΦA
        # Sociology & Psychology : AEA



