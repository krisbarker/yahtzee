#!/usr/bin/env python3


import random


def roll_the_dice(to_throw):
    die = [1, 2, 3, 4, 5, 6]
    thrown_list = []
    for i in range(0, to_throw):
        num = random.choice(die)
        thrown_list.append(num)
    return thrown_list
