import random

KILLERS = {
    "Michael Myers": 7,
    "Jason Vorhees": 6,
    "Freddy Krueger": 8,
    "Jigsaw": 2,
    "Pinhead": 9,
    "Leatherface": 5,
    "Ghostface": 3,
    "Hannibal Lecter": 4,
}


def get_killer():
    return random.choice(list(KILLERS.keys()))


def killer_battle(k1, k2):
    if k1 not in KILLERS:
        return
    if k2 not in KILLERS:
        return True
    return KILLERS[k1] > KILLERS[k2]


def random_pair():
    k1 = get_killer()
    k2 = get_killer()
    while k2 == k1:
        k2 = get_killer()
    return k1, k2
