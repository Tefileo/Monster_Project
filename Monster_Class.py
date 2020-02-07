class Monster():

    def __init__(self, name= 'No Name' ,strength = 'No Strength' ,scary_skill='No Skills'  ):
        self.name = name
        self.strength = strength
        self.scary_skill = scary_skill

    def eat(self, food=''): #makes the argument optional
        return 'nom nom nom nom '+food

    def sleep(self):
        return 'zzzzzz'

    def pay_taxes(self):
        return 'o_o .......... HUMMMM!!!! ---- O_O ----- SPLOSH'

    def shout_strength(self):
        return 'ATTTAACCKKK!!'