#!/usr/bin/env python3

"""
This should define a class that keeps the details about the game:
- Number of players
- Players Names
"""

from .players_class import Players


class TheGame:
    def __init__(self, number_of_players: int = None):
        self.throws = 0
        self.players_list = []
        if number_of_players is None:
            self.number_of_players = self.get_number_of_players()
        else:
            self.number_of_players = number_of_players
        self.get_players_names()

    @staticmethod
    def get_number_of_players():
        player_number_entry = int(input("How many players? "))
        while player_number_entry < 1 or player_number_entry > 4:
            print("You must choose a number of players between 1 - 4.")
            print("Please try again")
            player_number_entry = int(input("How many players? "))

        return player_number_entry

    def get_players_names(self):
        for i in range(1, (self.number_of_players + 1)):
            player_name = input(f"Please enter a name for Player {i}? ")
            player_name = Players(player_name, i, 0)
            self.players_list.append(player_name)
