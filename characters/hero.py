from characters.fighter import General_Fighter


class Hero(General_Fighter):
    __upper_cut = False
    __left_leg = False
    __right_leg = False
    __side_hook = False

    def __init__(self, name):
        super().__init__(name)

    def special_abilities(self, left_punch, right_punch, upper_cut, left_leg, right_leg, side_hook):
        super().special_abilities(left_punch, right_punch)
        self.__upper_cut = upper_cut
        self.__right_leg = right_leg
        self.__left_leg = left_leg
        self.__side_hook = side_hook

        return "Special Abilities"

    def lets_fight(self):
        print("I am hero and also")
        super().lets_fight()
        print("3. ", self.__upper_cut)
        print("4. ", self.__left_leg)
        print("5. ", self.__right_leg)
        print("6. ", self.__side_hook)
