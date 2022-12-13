#!/usr/bin/env python3


def bonus_check(player):
    if player.get_bonus_data("got") == "no":
        bonus_total_check = 0
        if player.get_ones_data("got") == "yes":
            bonus_total_check += int(player.get_ones_data("score"))
        if player.get_twos_data("got") == "yes":
            bonus_total_check += int(player.get_twos_data("score"))
        if player.get_threes_data("got") == "yes":
            bonus_total_check += int(player.get_threes_data("score"))
        if player.get_fours_data("got") == "yes":
            bonus_total_check += int(player.get_fours_data("score"))
        if player.get_fives_data("got") == "yes":
            bonus_total_check += int(player.get_fives_data("score"))
        if player.get_sixes_data("got") == "yes":
            bonus_total_check += int(player.get_sixes_data("score"))
        if bonus_total_check >= 63:
            player.set_bonus_value("score", 35)
            player.set_bonus_value("got", "yes")
            player.total_score += 35
    return

