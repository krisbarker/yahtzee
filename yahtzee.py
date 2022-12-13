#!/usr/bin/env python3

"""  Simple CLI-based Yahtzee game  """

from os import system, name
from time import sleep

from files.player import Players
from files.play_turn import play_a_turn
from files.scorecard_update import scorecard_entry


def start_the_game(number_of_players, player_list):
    """
    Creates the Players in the game
    Creates the scorecards for the Players
    """
    while True:
        try:
            number_of_players = int(input("How many players? "))
            if number_of_players > 4 or number_of_players < 1:
                print("You must choose a number of players between 1 - 4.")
                print("Please try again")
                start_the_game(number_of_players, player_list)
            elif number_of_players == "":
                raise Exception
            else:
                nop_counter = number_of_players + 1
                counter = 0
                for nop in range(1, nop_counter):
                    counter += 1
                    nop = str(nop)
                    player_name = input(f"Please enter a name for Player {nop}? ")
                    player_name = Players(
                        player_name,
                        counter,
                        {"got": "no", "score": "None"},  # Ones
                        {"got": "no", "score": "None"},  # Twos
                        {"got": "no", "score": "None"},  # Threes
                        {"got": "no", "score": "None"},  # Fours
                        {"got": "no", "score": "None"},  # Fives
                        {"got": "no", "score": "None"},  # Sixes
                        {"got": "no", "score": "None"},  # Bonus
                        {"got": "no", "score": "None"},  # Three of a Kind
                        {"got": "no", "score": "None"},  # Four of a Kind
                        {"got": "no", "score": "None"},  # Full House
                        {"got": "no", "score": "None"},  # Small Straight
                        {"got": "no", "score": "None"},  # Large Straight
                        {
                            "got": "no",
                            "y-1": "None",
                            "y-2": "None",
                            "y-3": "None",
                        },  # Yahtzee
                        {"got": "no", "score": "None"},  # Chance
                        0,  # Total Score
                        0,
                    )  # Bonus Throws
                    player_list.append(player_name)
        except Exception:
            continue
        return number_of_players, player_list


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


def we_have_a_winner(players):
    """
    Sets the winner
    """
    winner_list = {}
    for player in players:
        winner_list.update({player.name: player.total_score})
    winner_list = sorted(winner_list.items(), key=lambda x: x[1], reverse=True)
    print("The Winners List is!!!")
    for person in winner_list:
        print(person[0], "\t", person[1])


def main():
    """
    Runs the game

    This manages the turns and score entries
    It covers the basic 13 turns of the game
    """
    number_of_players: int = 0
    player_list = []

    number_of_players, player_list = start_the_game(number_of_players, player_list)

    turns = 0
    while turns < 13:
        for player in player_list:
            sleep(1)
            clear()
            print("Hi", player.name, "it's your turn")
            print(player)
            player.scorecard_print()
            final_set = play_a_turn(5)
            print("Your final set is:", final_set)
            sleep(1)
            scorecard_entry(final_set, player)
        turns += 1

    clear()
    for player in player_list:
        player.scorecard_print()
        print("\n")

    we_have_a_winner(player_list)


if __name__ == "__main__":
    main()
