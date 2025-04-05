#!/usr/bin/env python3


def upper_section_value_check(final_set, value):
    value_to_add = 0
    for num in final_set:
        num = int(num)
        if num == value:
            value_to_add += num

    return value_to_add
