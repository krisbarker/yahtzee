#!/usr/bin/env python3


def select_dice_check(prompt):
    """This is to check that the dice to keep input is valid"""
    """It checks to see if the numbers are between 1-5 and not repeated"""
    while True:
        try:
            kept_list = []
            list = input(prompt)
            # TODO: Need to capture in here if the input contains letters
            for ele in list:
                if ele.isnumeric():
                    ele = int(ele)
                    kept_list.append(ele)
            for num in kept_list:
                if kept_list.count(num) > 1:
                    # print(kept_list.count(num), "of", num)
                    raise Exception("You should only enter a number once")
                elif num > 5 or num < 1:
                    raise Exception("The number should be between 1 and 5")
        except Exception:
            print(
                "You have either entered a number twice, "
                "or you have entered a number outside the range 1-5"
            )
            continue
        else:
            return kept_list
