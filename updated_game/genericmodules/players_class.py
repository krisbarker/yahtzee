#!/usr/bin/env python3

"""
This cover the Player object
- Name
- Player number
- Bonus Throws
"""

from .scoreboard_class import Scorecard


class Players:
    def __init__(self, name, player_number, bonus_throws):
        self.name = name
        self.player_number = player_number
        self.bonus_throws = bonus_throws
        self.scorecard = Scorecard()

    def __str__(self):
        return f"{self.name} is Player " \
               f"{self.player_number} with a score of " \
               f"{self.scorecard.calculate_total_score()}"
