#!/usr/bin/env python3


from files.upper_total import upper_scorecard_total
from files.lower_total import lower_scorecard_total


class Players:
    def __init__(
        self,
        name: str,
        player_number: int,
        ones: dict,
        twos: dict,
        threes: dict,
        fours: dict,
        fives: dict,
        sixes: dict,
        bonus: dict,
        threeofakind: dict,
        fourofakind: dict,
        fullhouse: dict,
        smallstraight: dict,
        largestraight: dict,
        yahtzee: dict,
        chance: dict,
        total_score: int,
        bonus_throws: int,
    ):
        self.name = name
        self.player_number = player_number
        self.ones = ones
        self.twos = twos
        self.threes = threes
        self.fours = fours
        self.fives = fives
        self.sixes = sixes
        self.bonus = bonus
        self.threeofakind = threeofakind
        self.fourofakind = fourofakind
        self.fullhouse = fullhouse
        self.smallstraight = smallstraight
        self.largestraight = largestraight
        self.yahtzee = yahtzee
        self.chance = chance
        self.total_score = total_score
        self.bonus_throws = bonus_throws

    def __str__(self):
        return f"{self.name} is Player " \
               f"{self.player_number} with a score of " \
               f"{self.total_score}"

    def __repr__(self):
        """
        Repr of the object
        """
        return f"{self.name} is Player " \
               f"{self.player_number} with a score of " \
               f"{self.total_score}"

    def get_ones_data(self, key):
        ones_value = self.ones.get(key)
        return ones_value

    def set_ones_value(self, key, value):
        self.ones.update({key: value})

    def get_twos_data(self, key):
        twos_value = self.twos.get(key)
        return twos_value

    def set_twos_value(self, key, value):
        self.twos.update({key: value})

    def get_threes_data(self, key):
        threes_value = self.threes.get(key)
        return threes_value

    def set_threes_value(self, key, value):
        self.threes.update({key: value})

    def get_fours_data(self, key):
        fours_value = self.fours.get(key)
        return fours_value

    def set_fours_value(self, key, value):
        self.fours.update({key: value})

    def get_fives_data(self, key):
        fives_value = self.fives.get(key)
        return fives_value

    def set_fives_value(self, key, value):
        self.fives.update({key: value})

    def get_sixes_data(self, key):
        sixes_value = self.sixes.get(key)
        return sixes_value

    def set_sixes_value(self, key, value):
        self.sixes.update({key: value})

    def get_bonus_data(self, key):
        bonus_value = self.bonus.get(key)
        return bonus_value

    def set_bonus_value(self, key, value):
        self.bonus.update({key: value})

    def get_threeofakind_data(self, key):
        threeofakind_value = self.threeofakind.get(key)
        return threeofakind_value

    def set_threeofakind_value(self, key, value):
        self.threeofakind.update({key: value})

    def get_fourofakind_data(self, key):
        fourofakind_value = self.fourofakind.get(key)
        return fourofakind_value

    def set_fourofakind_value(self, key, value):
        self.fourofakind.update({key: value})

    def get_fullhouse_data(self, key):
        fullhouse_value = self.fullhouse.get(key)
        return fullhouse_value

    def set_fullhouse_value(self, key, value):
        self.fullhouse.update({key: value})

    def get_smallstraight_data(self, key):
        smallstraight_value = self.smallstraight.get(key)
        return smallstraight_value

    def set_smallstraight_value(self, key, value):
        self.smallstraight.update({key: value})

    def get_largestraight_data(self, key):
        largestraight_value = self.largestraight.get(key)
        return largestraight_value

    def set_largestraight_value(self, key, value):
        self.largestraight.update({key: value})

    def get_yahtzee_data(self, key):
        yahtzee_value = self.yahtzee.get(key)
        return yahtzee_value

    def set_yahtzee_value(self, key, value):
        self.yahtzee.update({key: value})

    def get_chance_data(self, key):
        chance_value = self.chance.get(key)
        return chance_value

    def set_chance_value(self, key, value):
        self.chance.update({key: value})

    def get_total_score(self):
        return self.total_score

    def set_total_score(self, value):
        self.total_score += value

    def get_bonus_throws(self):
        return self.bonus_throws

    def set_bonus_throws(self, value):
        self.bonus_throws += value

    # TODO: Make the upperscorecard calculation work in the class
    def get_uppperscorecard_value(self):
        pass

    # TODO: Make the lowerscorecard calculation work in the class
    def get_lowerscorecard_value(self):
        pass

    def scorecard_print(self):
        print("This is the scorecard for: ", self.name)
        print("Ones: \t\t\t", self.get_ones_data("score"))
        print("Twos: \t\t\t", self.get_twos_data("score"))
        print("Threes: \t\t", self.get_threes_data("score"))
        print("Fours: \t\t\t", self.get_fours_data("score"))
        print("Fives: \t\t\t", self.get_fives_data("score"))
        print("Sixes: \t\t\t", self.get_sixes_data("score"))
        print("Bonus: \t\t\t", self.get_bonus_data("score"))
        print("Upper Total: \t\t", upper_scorecard_total(self))

        print("\nThree of a Kind: \t", self.get_threeofakind_data("score"))
        print("Four of a Kind:  \t", self.get_fourofakind_data("score"))
        print("Full House: \t\t", self.get_fullhouse_data("score"))
        print("Small Straight: \t", self.get_smallstraight_data("score"))
        print("Large Straight: \t", self.get_largestraight_data("score"))
        print(
            "Yahtzee: \t\t",
            self.get_yahtzee_data("y-1"),
            "\tYB1: \t",
            self.get_yahtzee_data("y-2"),
            "\tYB2: \t",
            self.get_yahtzee_data("y-3"),
        )
        print("Chance: \t\t", self.get_chance_data("score"))
        print("Lower Total: \t\t", lower_scorecard_total(self))
        print("\nTotal score of: ", self.total_score, " for ", self.name)
