#!/usr/bin/env python3


from .selected_check import select_dice_check


def dice_to_keep(orig_list, max_num, kl):
    print("\nWhich dice would you like to keep?")
    print("(If you wish to keep dice 1, 2 and 5 type: 1, 2, 5)")
    print("(If you don't want to keep any, type: 0 or just press 'return')")
    dtk = select_dice_check("Dice to keep? \t")
    for ele in dtk:
        ele = int(ele)
        ele -= 1
        kl.append(orig_list[ele])
    max_num = 5 - len(kl)
    return kl, max_num
