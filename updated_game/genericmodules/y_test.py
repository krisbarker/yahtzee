#!/usr/bin/env python3


def yahtzee_test(die_list):
    """This looks a little dirty and can be cleaner"""
    for elem in die_list:
        if die_list.count(elem) == 5:
            return 50
        else:
            print("Unfortunately you don't have a yahtzee, so  score 0")
            return 0
