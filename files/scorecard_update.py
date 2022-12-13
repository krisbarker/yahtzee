#!/usr/bin/env python3

from files.three_oak_test import three_of_a_kind_test
from files.four_oak_test import four_of_a_kind_test
from files.fh_test import full_house_test
from files.ss_test import small_straight_test
from files.ls_test import large_straight_test
from files.y_test import yahtzee_test
from files.chance_test import chance_test
from files.bonus_test import bonus_check


def scorecard_entry(working_dice, player):
    options_list = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "Three",
        "three",
        "Four",
        "four",
        "Full",
        "full",
        "SS",
        "ss",
        "LS",
        "ls",
        "Y",
        "y",
        "C",
        "c",
    ]
    while True:
        try:
            category_chosen = input(
                "\nWhat scorecard category do you want to use\n"
                "1s, 2s, 3s, 4s, 5s or 6s?\t OR\n"
                "Three, Four, Full, SS, LS, Y or C?   "
            )
            if category_chosen == "1":
                if player.get_ones_data("got") == "no":
                    value_to_add = 0
                    for num in working_dice:
                        num = int(num)
                        if num == 1:
                            value_to_add += num
                    player.set_ones_value("score", value_to_add)
                    player.set_ones_value("got", "yes")
                    player.total_score += value_to_add
                elif player.get_ones_data("got") == "yes":
                    raise Exception
            elif category_chosen == "2":
                if player.get_twos_data("got") == "no":
                    value_to_add = 0
                    for num in working_dice:
                        num = int(num)
                        if num == 2:
                            value_to_add += num
                    player.set_twos_value("score", value_to_add)
                    player.set_twos_value("got", "yes")
                    player.total_score += value_to_add
                elif player.get_twos_data("got") == "yes":
                    raise Exception
            elif category_chosen == "3":
                if player.get_threes_data("got") == "no":
                    value_to_add = 0
                    for num in working_dice:
                        num = int(num)
                        if num == 3:
                            value_to_add += num
                    player.set_threes_value("score", value_to_add)
                    player.set_threes_value("got", "yes")
                    player.total_score += value_to_add
                elif player.get_threes_data("got") == "yes":
                    raise Exception
            elif category_chosen == "4":
                if player.get_fours_data("got") == "no":
                    value_to_add = 0
                    for num in working_dice:
                        num = int(num)
                        if num == 4:
                            value_to_add += num
                    player.set_fours_value("score", value_to_add)
                    player.set_fours_value("got", "yes")
                    player.total_score += value_to_add
                elif player.get_fours_data("got") == "yes":
                    raise Exception
            elif category_chosen == "5":
                if player.get_fives_data("got") == "no":
                    value_to_add = 0
                    for num in working_dice:
                        num = int(num)
                        if num == 5:
                            value_to_add += num
                    player.set_fives_value("score", value_to_add)
                    player.set_fives_value("got", "yes")
                    player.total_score += value_to_add
                elif player.get_fives_data("got") == "yes":
                    raise Exception
            elif category_chosen == "6":
                if player.get_sixes_data("got") == "no":
                    value_to_add = 0
                    for num in working_dice:
                        num = int(num)
                        if num == 6:
                            value_to_add += num
                    player.set_sixes_value("score", value_to_add)
                    player.set_sixes_value("got", "yes")
                    player.total_score += value_to_add
                elif player.get_sixes_data("got") == "yes":
                    raise Exception
            elif category_chosen == "Three" or category_chosen == "three":
                if player.get_threeofakind_data("got") == "no":
                    value_to_add = three_of_a_kind_test(working_dice)
                    player.set_threeofakind_value("score", value_to_add)
                    player.set_threeofakind_value("got", "yes")
                    player.total_score += value_to_add
                elif player.get_threeofakind_data("got") == "yes":
                    raise Exception
            elif category_chosen == "Four" or category_chosen == "four":
                if player.get_fourofakind_data("got") == "no":
                    value_to_add = four_of_a_kind_test(working_dice)
                    player.set_fourofakind_value("score", value_to_add)
                    player.set_fourofakind_value("got", "yes")
                    player.total_score += value_to_add
                elif player.get_fourofakind_data("got") == "yes":
                    raise Exception
            elif category_chosen == "Full" or category_chosen == "full":
                if player.get_fullhouse_data("got") == "no":
                    value_to_add = full_house_test(working_dice)
                    player.set_fullhouse_value("score", value_to_add)
                    player.set_fullhouse_value("got", "yes")
                    player.total_score += value_to_add
                elif player.get_fullhouse_data("got") == "yes":
                    raise Exception
            elif category_chosen == "SS" or category_chosen == "ss":
                if player.get_smallstraight_data("got") == "no":
                    value_to_add = small_straight_test(working_dice)
                    player.set_smallstraight_value("score", value_to_add)
                    player.set_smallstraight_value("got", "yes")
                    player.total_score += value_to_add
                elif player.get_smallstraight_data("got") == "yes":
                    raise Exception
            elif category_chosen == "LS" or category_chosen == "ls":
                if player.get_largestraight_data("got") == "no":
                    value_to_add = large_straight_test(working_dice)
                    player.set_largestraight_value("score", value_to_add)
                    player.set_largestraight_value("got", "yes")
                    player.total_score += value_to_add
                elif player.get_largestraight_data("got") == "yes":
                    raise Exception
            elif category_chosen == "Y" or category_chosen == "y":
                if player.get_yahtzee_data("got") == "no":
                    value_to_add = yahtzee_test(working_dice)
                    player.set_yahtzee_value("y-1", value_to_add)
                    player.set_yahtzee_value("got", "yes")
                    player.total_score += int(value_to_add)
                    # if player.get_bonus_throws < 2:
                    # player.bonus_throws += 1
                elif player.get_yahtzee_data("got") == "yes":
                    raise Exception
            elif category_chosen == "C" or category_chosen == "c":
                if player.get_chance_data("got") == "no":
                    value_to_add = chance_test(working_dice)
                    player.set_chance_value("score", value_to_add)
                    player.set_chance_value("got", "yes")
                    player.total_score += value_to_add
                elif player.get_chance_data("got") == "yes":
                    raise Exception
            elif category_chosen not in options_list:
                continue
            elif category_chosen == "":
                continue
        except Exception:
            print("\n\t !!!  You've already used that category  !!!")
            continue
        else:
            # This inspects for, and adds where applicable, a bonus to the upper score card
            bonus_check(player)
            break
