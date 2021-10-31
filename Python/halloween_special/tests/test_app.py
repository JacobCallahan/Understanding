import pytest
from my_app import app
from my_app import helpers

@pytest.fixture(scope="session")
def session_killer():
    yield helpers.get_killer()


def test_winning_message(session_killer):
    import helpers as test_helpers
    worse_killer = test_helpers.get_worse_killer()
    res = app.run_scenario(session_killer, worse_killer)
    assert res == f"{session_killer} slaughtered {worse_killer}"


def test_losing_message(session_killer):
    import helpers as test_helpers
    better_killer = test_helpers.get_better_killer()
    res = app.run_scenario(session_killer, better_killer)
    assert res == f"{better_killer} decimated {session_killer}"
