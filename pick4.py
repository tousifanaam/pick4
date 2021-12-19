from random import randint
from typing import Iterable


def pick(n: int = 9, start: int = 0, total_pick: int = 4):
    """
    default> start value: 0 (included)
    default> end value: 9 (included)
    default> total number of selection: 4
    """
    return tuple([randint(start, n) for _ in range(total_pick)])


def straight(draw_pick: tuple, pick: tuple):
    """
    All four digits must match the digits drawn in the exact same order
    """
    return pick == draw_pick


def box(draw_pick: tuple, pick: tuple):
    """
    All four digits must match the digits drawn in any order
    """
    return len([i for i in pick if i in draw_pick]) == 4 and len([i for i in draw_pick if i in pick]) == 4


def four_way_box(draw_pick: tuple, pick: tuple):
    """
    All four digits must match the digits drawn in any order, 
    where three of the digits are the same
    """
    if 3 in [draw_pick.count(i) for i in draw_pick[:-2]]:
        return box(draw_pick=draw_pick, pick=pick)
    return False


def six_way_box(draw_pick: tuple, pick: tuple):
    """
    All four digits must match the digits drawn in any order, 
    where two sets of digits are the same
    """
    if len(set(draw_pick)) == 2:
        return box(draw_pick=draw_pick, pick=pick)
    return False


def twelve_way_box(draw_pick: tuple, pick: tuple):
    """
    All four digits must match the digits drawn in any order, 
    where two of the digits are the same
    """
    if [i for i in draw_pick if draw_pick.count(i) >= 2]:
        return box(draw_pick=draw_pick, pick=pick)
    return False


def twenty_four_way_box(draw_pick: tuple, pick: tuple):
    """
    All four digits must match the digits drawn in any order, 
    where all 4 digits are different
    """
    if len(set(draw_pick)) == 4:
        return box(draw_pick=draw_pick, pick=pick)
    return False


if __name__ == "__main__":

    from sys import argv

    winning_numbers, my_pick = pick(), pick()
    if "-s" in argv or "--selfpick" in argv:
        my_pick = tuple([int(i) for i in input(
            "Choose 4 numbers, where range: [0,9], eg. 1172> ")])
    print(f"win: {winning_numbers} | choice: {my_pick}")
    print(f"1> Straight  : {straight(winning_numbers, my_pick)}")
    print(f"2> Box       : {box(winning_numbers, my_pick)}")
    print(f"3> 4 way box : {four_way_box(winning_numbers, my_pick)}")
    print(f"4> 6 way box : {six_way_box(winning_numbers, my_pick)}")
    print(f"5> 12 way box: {twelve_way_box(winning_numbers, my_pick)}")
    print(f"6> 24 way box: {twenty_four_way_box(winning_numbers, my_pick)}")

    exit()

    from os import system, name

    def clear():
        if name == "nt":
            _ = system("cls")
        else:
            _ = system("clear")

    def run_funcs(func_list: Iterable, *args):
        for i in func_list:
            print(f"{i.__name__}() > {i(*args)}")

    winning_numbers = pick()
    while True:
        my_pick = pick()
        print(f"win: {winning_numbers} | choice: {my_pick}")
        run_funcs([straight, box, four_way_box, six_way_box,
                   twelve_way_box, twenty_four_way_box], winning_numbers, my_pick)
        clear()