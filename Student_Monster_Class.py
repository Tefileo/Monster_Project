from Monster_Class import Monster

class Student_Monster(Monster):

    def __init__(self, uni_id='000000',scary_subjects='Scary101, Shouting102' ):
        self.uni_id = uni_id
        self.scary_subjects = scary_subjects

    def run(self):
        return 'Wooosh'

    def jump(self):
        return 'OOOOFTTTT'

    def scare(self):
        return 'ROOARRRRR'