import gc
import inspect
from functools import wraps
from _pytest.fixtures import FixtureManager


class FixtureFinder:
    _fixture_manager = None

    @property
    def fixture_manager(self):
        """Find references to pytest's FixtureManager or raise and exception"""
        if not self._fixture_manager:
            self._fixture_manager = [
                f for f in gc.get_objects() if isinstance(f, FixtureManager)
            ][0]
        if not self._fixture_manager:
            raise Exception("Attempted to use FixtureManager outside of pytest session.")
        return self._fixture_manager

    def find_fixture_val(self, fixture_name):
        """Find the value for an already resolved fixture"""
        if fixture := self.fixture_manager._arg2fixturedefs.get(fixture_name, None):
            if cached_result := fixture[0].cached_result:
                return cached_result[0]

    def resolve_fixtures(self):
        """Find and fill the values for fixtures in the caller's argpsec"""
        caller = inspect.currentframe().f_back
        for var_name in caller.f_locals.keys():
            if resolved := self.find_fixture_val(var_name):
                caller.f_locals[var_name] = resolved

    def use_fixtures(self, func):
        """Decorator that resolves the fixtures in a function's argspec"""
        resolved_fixtures = {}
        for param in inspect.signature(func).parameters:
            if f_val := self.find_fixture_val(param):
                resolved_fixtures[param] = f_val

        @wraps(func)
        def wrapper(*args, **kwargs):
            kwargs.update(resolved_fixtures)
            return func(*args, **kwargs)

        return wrapper


fixture_finder = FixtureFinder()
