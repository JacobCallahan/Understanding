"""Argparse removes the hassle of manually parsing and helps validate input"""

import argparse

SIZES = {
    "s": "Small",
    "m": "Medium",
    "l": "Large",
    "xl": "Extra large",
    "xxl": "Extra extra large"
}

CRUSTS = {"normal": "", "thin": " thin crust", "deep": " deep dish"}


def build_pizza(order):
    pizza = f"{SIZES[order.size]}{CRUSTS[order.crust]}"
    if order.toppings:
        pizza +=  " with " + ", ".join(order.toppings)
    if order.cheese:
        pizza += " plus extra cheese"
    if order.sauce:
        pizza += " and extra sauce"
    return pizza


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Welcome to the pizza builder, let's build a pizza!!")
    parser.add_argument(
        "size",
        type=str,
        choices=SIZES.keys(),
        help="Size of your pizza"
    )
    parser.add_argument(
        "crust",
        type=str,
        choices=CRUSTS.keys(),
        help="Type of pizza crust"
    )
    parser.add_argument(
        "-t", "--toppings",
        type=str,
        nargs="+",
        help="One or more toppings for your pizza"
    )
    parser.add_argument(
        "--extra-cheese",
        action="store_true",
        dest="cheese",
        help="Add extra cheese to your pizza"
    )
    parser.add_argument(
        "--extra-sauce",
        action="store_true",
        dest="sauce",
        help="Add extra sauce to your pizza"
    )
    parsed_args = parser.parse_args()
    pizza = build_pizza(parsed_args)
    print(f"Your pizza is: {pizza}!!")
