#!/usr/bin/env python3


def lower_scorecard_total(player):
    lower_running_total = 0
    if player.get_threeofakind_data("got") == "yes":
        lower_running_total += player.get_threeofakind_data("score")
    if player.get_fourofakind_data("got") == "yes":
        lower_running_total += player.get_fourofakind_data("score")
    if player.get_fullhouse_data("got") == "yes":
        lower_running_total += player.get_fullhouse_data("score")
    if player.get_smallstraight_data("got") == "yes":
        lower_running_total += player.get_smallstraight_data("score")
    if player.get_largestraight_data("got") == "yes":
        lower_running_total += player.get_largestraight_data("score")
    if player.get_yahtzee_data("got") == "yes":
        lower_running_total += player.get_yahtzee_data("y-1")
    if player.get_chance_data("got") == "yes":
        lower_running_total += player.get_chance_data("score")
    return lower_running_total
