from random import randint
from typing import Iterable


def arg_check(func):

    def wrapper(*args, **kwargs):

        if len(args) == 2:
            if not isinstance(args[0], tuple):
                args[0] = tuple(args[0])
            if not isinstance(args[1], tuple):
                args[1] = tuple(args[1])
            foo1 = [i for i in args[0] if not isinstance(i, int)]
            foo2 = [i for i in args[1] if not isinstance(i, int)]
            if len(foo1) != 0 or len(foo2) != 0:
                raise ValueError(
                    f"invalid literal for int() with base 10: {', '.join(foo1 + foo2)}")

        return func(*args, **kwargs)

    return wrapper


def pick(n: int = 9, start: int = 0, total_pick: int = 4):
    """
    default> start value: 0 (included)
    default> end value: 9 (included)
    default> total number of selection: 4
    """
    return tuple([randint(start, n) for _ in range(total_pick)])


@arg_check
def straight(draw_pick: tuple, pick: tuple):
    """
    All four digits must match the digits drawn in the exact same order
    """
    return pick == draw_pick


@arg_check
def box(draw_pick: tuple, pick: tuple):
    """
    All four digits must match the digits drawn in any order
    """
    return set(draw_pick) == set(pick)


@arg_check
def four_way_box(draw_pick: tuple, pick: tuple):
    """
    All four digits must match the digits drawn in any order, 
    where three of the digits are the same
    """
    if 3 in [draw_pick.count(i) for i in draw_pick[:-2]] or len(set(draw_pick)) == 4:
        return box(draw_pick=draw_pick, pick=pick)
    return False


@arg_check
def six_way_box(draw_pick: tuple, pick: tuple):
    """
    All four digits must match the digits drawn in any order, 
    where two sets of digits are the same
    """
    if len(set(draw_pick)) == 2:
        return box(draw_pick=draw_pick, pick=pick)
    return False


@arg_check
def twelve_way_box(draw_pick: tuple, pick: tuple):
    """
    All four digits must match the digits drawn in any order, 
    where two of the digits are the same
    """
    if [i for i in draw_pick if draw_pick.count(i) >= 2]:
        return box(draw_pick=draw_pick, pick=pick)
    return False


@arg_check
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
