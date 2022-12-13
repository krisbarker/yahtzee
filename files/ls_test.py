#!/usr/bin/env python3


def large_straight_test(die_list):
    ls1 = [1, 2, 3, 4, 5]
    ls2 = [2, 3, 4, 5, 6]

    die_list = sorted(die_list)

    if die_list == ls1 or die_list == ls2:
        return 40
    else:
        print("Unfortunately you didn't have a large straight, so score 0")
        return 0
