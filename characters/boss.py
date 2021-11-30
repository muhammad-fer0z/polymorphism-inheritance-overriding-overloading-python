from characters.fighter import General_Fighter


class Boss(General_Fighter):
    __side_skip = False
    __left_leg = False
    __right_leg = False
    __side_hook = False

    def __init__(self, name):
        super().__init__(name)

    def special_abilities(self, left_punch, right_punch, side_skip, left_leg, right_leg, side_hook):
        super().special_abilities(left_punch, right_punch)
        self.__side_skip = side_skip
        self.__right_leg = right_leg
        self.__left_leg = left_leg

    def lets_fight(self):
        print("I am Boss and also")
        super().lets_fight()
        print("3. ", self.__side_skip)
        print("4. ", self.__left_leg)
        print("5. ", self.__right_leg)
