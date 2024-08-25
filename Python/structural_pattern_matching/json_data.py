"""Working with API data just became much easier!"""
POKEMON = [
    {
        "name": "Pikachu",
        "type": "Electric",
        "attack": 55,
        "defense": 40,
        "abilities": ["Static", "Lightning Rod"],
    },
    {
        "name": "Charmander",
        "type": "Fire",
        "attack": 52,
        "defense": 43,
        "abilities": ["Blaze", "Solar Power"],
    },
    {
        "type": "Fire",
        "attack": 38,
        "defense": 41,
        "abilities": ["Flash Fire", "Snow Warning"],
    },
    {
        "name": "Squirtle",
        "type": "Water",
        "attack": 48,
        "defense": 65,
        "abilities": ["Torrent", "Rain Dish"],
    },
    {
        "name": "Eevee",
        "type": "Normal",
        "attack": 57,
        "defense": 53,
        "abilities": ["Run Away", "Adaptability"],
    },
]


class Vars: pass


def get_by_type(p_type):
    Vars.type = p_type
    results = {}
    for mon in POKEMON:
        match mon:
            case {"name": name, "type": Vars.type, "abilities": abilities}:
                results[name] = abilities
    return results
