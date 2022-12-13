#!/usr/bin/env python3


def four_of_a_kind_test(die_list):
    for x in range(1, 7):
        y = die_list.count(x)
        if y >= 4:
            score = 0
            for elem in die_list:
                score += elem
            return score
    print("Unfortunately you didn't have three of a kind, so score 0")
    return 0
