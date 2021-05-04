"""You can manually process command line input as a list via sys.argv"""

import sys


SIZES = {
    "s": "Small",
    "m": "Medium",
    "l": "Large",
    "xl": "Extra large",
    "xxl": "Extra extra large"
}

CRUSTS = {"normal": "", "thin": " thin crust", "deep": " deep dish"}


def print_help():
    """Print help text and exit"""
    print(
        f"""Welcome to the pizza builder, let's build a pizza!

    Usage: pizza_builder.py [ARGS] [OPTIONS]

    Arguments:
      size           {", ".join(SIZES.keys())}
      crust          {", ".join(CRUSTS.keys())}

    Options:
      --toppings     One or more toppings for your pizza
      --extra-cheese Add extra cheese to your pizza
      --extra-sauce  Add extra sauce to your pizza
      -h, --help     Print help text and exit
    """
    )
    sys.exit(0)


def process_input(args_list):
    args_list.pop(0)
    order_dict = {"size": args_list.pop(0), "crust": args_list.pop(0), "toppings": []}
    if "--extra-cheese" in args_list:
        order_dict["extra-cheese"] = True
        args_list.remove("--extra-cheese")
    if "--extra-sauce" in args_list:
        order_dict["extra-sauce"] = True
        args_list.remove("--extra-sauce")
    if "--toppings" in args_list:
        args_list.remove("--toppings")
        order_dict["toppings"] = args_list
    return order_dict


def validate_input(processed):
    valid = True
    if processed["size"] not in SIZES.keys():
        print(f"Invalid size choice: {processed['size']}")
        valid = False
    if processed["crust"] not in CRUSTS.keys():
        print(f"Invalid crust choice: {processed['crust']}")
        valid = False
    for topping in processed["toppings"]:
        if topping.startswith("-"):
            print(f"Invalid topping choice: {topping}")
            valid = False
    if not valid:
        print_help()


def build_pizza(order):
    pizza = f"{SIZES[order['size']]}{CRUSTS[order['crust']]}"
    if order.get("toppings"):
        pizza +=  " with " + ", ".join(order["toppings"])
    if order.get("extra-cheese"):
        pizza += " plus extra cheese"
    if order.get("extra-sauce"):
        pizza += " and extra sauce"
    return pizza


if __name__ == "__main__":
    if "--help" in sys.argv or "-h" in sys.argv or len(sys.argv) < 3:
        print_help()
    # print(sys.argv)
    processed_order = process_input(sys.argv)
    validate_input(processed_order)
    # print(processed_order)
    pizza = build_pizza(processed_order)
    print(f"Your pizza is: {pizza}!!")
