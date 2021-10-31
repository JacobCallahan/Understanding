from my_app import helpers
from my_app.ssshhh import fixture_finder


@fixture_finder.use_fixtures
def get_better_killer(session_killer):
    new_killer = helpers.get_killer()
    tries = 10
    while helpers.killer_battle(session_killer, new_killer) and tries:
        new_killer = helpers.get_killer()
        tries -= 1
    return new_killer


@fixture_finder.use_fixtures
def get_worse_killer(session_killer):
    new_killer = helpers.get_killer()
    tries = 10
    while not helpers.killer_battle(session_killer, new_killer) and tries:
        new_killer = helpers.get_killer()
        tries -= 1
    return new_killer
