#!/usr/bin/env python3


def upper_scorecard_total(player):
    upper_running_total = 0
    if player.get_ones_data("got") == "yes":
        upper_running_total += int(player.get_ones_data("score"))
    if player.get_twos_data("got") == "yes":
        upper_running_total += int(player.get_twos_data("score"))
    if player.get_threes_data("got") == "yes":
        upper_running_total += int(player.get_threes_data("score"))
    if player.get_fours_data("got") == "yes":
        upper_running_total += int(player.get_fours_data("score"))
    if player.get_fives_data("got") == "yes":
        upper_running_total += int(player.get_fives_data("score"))
    if player.get_sixes_data("got") == "yes":
        upper_running_total += int(player.get_sixes_data("score"))
    if player.get_bonus_data("got") == "yes":
        upper_running_total += int(player.get_bonus_data("score"))
    return upper_running_total
