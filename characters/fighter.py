class General_Fighter:
    __left_punch = False
    __right_punch = False

    def __init__(self, name):
        self.name = name

    def special_abilities(self, left_punch, right_punch):
        self.__left_punch = left_punch
        self.__right_punch = right_punch

        return "Special Abilities"

    def lets_fight(self):
        print("I am fighter.")
        print("---Special Abilities---")
        print("1. ", self.__left_punch)
        print("2. ", self.__right_punch)
