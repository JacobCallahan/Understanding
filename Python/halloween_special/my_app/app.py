"""This is my super amazing app that will definitely make me rich!"""
from my_app import helpers


def run_scenario(k1=None, k2=None):
    if not k1:
        k1 = input("Enter a killer's name or your own: ")
        k1 = k1 or helpers.get_killer()
    if not k2:
        k2 = input("Enter a killer's name or your own: ")
        k2 = k2 or helpers.get_killer()
    if helpers.killer_battle(k1, k2):
        return f"{k1} slaughtered {k2}"
    else:
        return f"{k2} decimated {k1}"


def run_app():
    print(run_scenario())

if __name__ == "__main__":
    run_app()