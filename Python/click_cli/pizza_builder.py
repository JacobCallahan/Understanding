"""Click uses decorators to define a CLI"""

import click

SIZES = {
    "s": "Small",
    "m": "Medium",
    "l": "Large",
    "xl": "Extra large",
    "xxl": "Extra extra large"
}

CRUSTS = {"normal": "", "thin": " thin crust", "deep": " deep dish"}

@click.command()
@click.argument("size", type=click.Choice(SIZES.keys()), default="l")
@click.argument("crust", type=click.Choice(CRUSTS.keys()), default="normal")
@click.option("-t", "--toppings", type=str, multiple=True, help="One or more toppings for your pizza")
@click.option("--extra-cheese", "cheese", is_flag=True, help="Add extra cheese to your pizza")
@click.option("--extra-sauce", "sauce", is_flag=True, help="Add extra sauce to your pizza")
def build_pizza(size, crust, toppings, cheese, sauce):
    """Welcome to the pizza builder, let's build a pizza!!"""
    pizza = f"{SIZES[size]}{CRUSTS[crust]}"
    if toppings:
        pizza +=  " with " + ", ".join(toppings)
    if cheese:
        pizza += " plus extra cheese"
    if sauce:
        pizza += " and extra sauce"
    click.echo(f"Your pizza is: {pizza}!!")


if __name__ == "__main__":
    build_pizza()
