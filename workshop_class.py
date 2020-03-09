from monster_class import *

class Workshop(Monster):

    def __init__(self, teacher_id, subject, list_of_attendees):
        self.teacher_id = teacher_id # SHOULD BE PRIVATE __teacher_id
        self.subject = subject
        self.list_of_attendees = list_of_attendees

