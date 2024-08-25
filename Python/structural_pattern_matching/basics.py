"""Structural Pattern Matching is a powerful replacement for if/elif/else"""
import random


match random.randint(0, 10):
    case 5:
        print("Lucky!")
    case 4 | 6 as num:
        print(f"You got close with {num}!")
    case num if num % 2 != 0:
        print(f"at least {num} was odd.")
    case miss:
        print(f"You missed with {miss}!")
