#!/usr/bin/env python3

"""
This should define a class that keeps the details about the game:
- Number of players
- Players Names
"""

from .upper_section_value_check import upper_section_value_check
from .three_oak_test import three_of_a_kind_test
from .four_oak_test import four_of_a_kind_test
from .fh_test import full_house_test
from .ss_test import small_straight_test
from .ls_test import large_straight_test
from .y_test import yahtzee_test
from .chance_test import chance_test


def test_and_update(category_chosen, category_name, test_function, player, final_set,  value=0):
    """
    This function should take a category and return the value of that category.
    It should also update the category.
    """

    upper_list = ["1", "2", "3", "4", "5", "6"]
    if category_chosen in upper_list:
        if player.scorecard.upper_section[category_name] == 0:
            value_to_add = test_function(final_set, value)
            player.scorecard.upper_section[category_name] = value_to_add
        else:
            print(f"You can't choose this category")
            choose_a_category(player, final_set)
    else:
        if player.scorecard.lower_section[category_name] == 0:
            value_to_add = test_function(final_set)
            player.scorecard.lower_section[category_name] = value_to_add
        else:
            print(f"You can't choose this category")
            choose_a_category(player, final_set)


def update_a_category(category_chosen, player: object, final_set, value=0):
    """

    Args:
        category_chosen:
        value:
        final_set (object):
        player (object):
    """
    categories_map = {
        "1": ("ones", upper_section_value_check),
        "2": ("twos", upper_section_value_check),
        "3": ("threes", upper_section_value_check),
        "4": ("fours", upper_section_value_check),
        "5": ("fives", upper_section_value_check),
        "6": ("sixes", upper_section_value_check),
        "Three": ("three_of_a_kind", three_of_a_kind_test),
        "Four": ("four_of_a_kind", four_of_a_kind_test),
        "Full": ("full_house", full_house_test),
        "SS": ("small_straight", small_straight_test),
        "LS": ("large_straight", large_straight_test),
        "Y": ("yahtzee", yahtzee_test),
        "C": ("chance", chance_test),
    }

    if category_chosen in categories_map:
        category_name, test_function = categories_map[category_chosen]
        test_and_update(category_chosen, category_name, test_function, player, final_set,  value)
    else:
        print("Invalid category chosen")
        choose_a_category(player, final_set)


def choose_a_category(player, final_set):
    category_chosen = input(
        "\nWhat scorecard category do you want to use\n"
        "1s, 2s, 3s, 4s, 5s or 6s?\t OR\n"
        "Three, Four, Full, SS, LS, Y or C?"
    )

    upper_list = ["1", "2", "3", "4", "5", "6"]

    print(type(category_chosen), category_chosen)

    if category_chosen in upper_list:
        value = int(category_chosen)
    else:
        value = 0

    update_a_category(category_chosen, player, final_set, value)
