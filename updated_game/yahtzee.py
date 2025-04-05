#!/usr/bin/env python3

"""
This is the updated game.  Written whilst on a plane from Abu Dhabi
I was meant to be doing some work, but the wifi wasn't working

This will start and control the game
"""

from os import system, name
from time import sleep

from genericmodules.yahtzee_artwork import get_artwork_string
from genericmodules.start_the_game import TheGame
from genericmodules.choose_a_category import choose_a_category

from genericmodules.play_turn import play_a_turn


def clear():
    """
    Clears the screen depending on OS type
    """
    # for windows
    if name == "nt":
        _ = system("cls")
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


def main():
    artwork = get_artwork_string()
    print(artwork)

    this_game = TheGame()

    """
    for player in this_game.players_list:
        print(player.name, player.bonus_throws)
        print(player.scorecard.display_scorecard())
    """

    while this_game.throws < 13:
        for player in this_game.players_list:
            sleep(2)
            clear()
            print("Hi", player.name, "it's your turn")
            print(player)
            print(player.scorecard.display_scorecard())

            final_set = play_a_turn(5)
            print("Your final set is:", final_set)

            choose_a_category(player, final_set)

            this_game.throws += 1

    # TODO do something at the game end


if __name__ == '__main__':
    main()
