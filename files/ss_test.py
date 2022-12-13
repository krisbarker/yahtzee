#!/usr/bin/env python3


def small_straight_test(die_list):
    ss1 = {1, 2, 3, 4}
    ss2 = {2, 3, 4, 5}
    ss3 = {3, 4, 5, 6}

    for dice in die_list:
        if die_list.count(dice) > 1:
            die_list.remove(dice)

    if set(die_list).intersection(ss1) == ss1 or \
            set(die_list).intersection(ss2) == ss2 or \
            set(die_list).intersection(ss3) == ss3:
        return 30
    else:
        print("Unfortunately you didn't have a small straight, so score 0")
        return 0


def main():
    thrown = [3, 2, 4, 5, 4]
    answer = small_straight_test(thrown)
    print(f"Answer is: {answer}")


if __name__ == "__main__":
    main()
