#!/usr/bin/env python3


def full_house_test(die_list):
    die_list = sorted(die_list)
    if (
        die_list[0] == die_list[1]
        and die_list[2] == die_list[3] == die_list[4]
        or die_list[0] == die_list[1] == die_list[2]
        and die_list[3] == die_list[4]
    ):
        return 25
    else:
        print("Unfortunately you didn't have a full house, so score 0")
        return 0
