#!/usr/bin/env python3


from .aroll import roll_the_dice
from .dice_choice import dice_to_keep


def play_a_turn(nofdtot):
    global thrown
    num_of_dice_to_throw = nofdtot
    kept_list = []
    for roll in range(0, 3):
        if roll == 0:  # or roll == 1:
            thrown = roll_the_dice(num_of_dice_to_throw)
            print("\n")
            for j in range(0, num_of_dice_to_throw):
                print("Dice ", j + 1, " is ", thrown[j])
            kept_list, num_of_dice_to_throw = dice_to_keep(
                thrown, num_of_dice_to_throw, kept_list
            )
            if len(kept_list) == 5:
                break
        elif roll == 1:
            print("\n")
            new_t_list = []
            num_of_dice_to_throw = 5 - len(kept_list)
            thrown = roll_the_dice(num_of_dice_to_throw)
            for j in range(0, num_of_dice_to_throw):
                print("Dice ", j + 1, " is ", thrown[j])
                new_t_list.append(thrown[j])
            for k in range(0, len(kept_list)):
                print("Kept list dice:", k + 1, "is", kept_list[k])
                new_t_list.append(kept_list[k])
            kept_list = []
            kept_list, num_of_dice_to_throw = dice_to_keep(
                new_t_list, num_of_dice_to_throw, kept_list
            )
            if len(kept_list) == 5:
                break
        else:
            print("This is the third, and final, throw!")
            thrown = roll_the_dice(num_of_dice_to_throw)
            for ele in thrown:
                kept_list.append(ele)
        roll += 1
    return kept_list
