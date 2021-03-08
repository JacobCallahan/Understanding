"""
Exceptions are errors encountered while running a program
try/except allows you to handle exceptions
"""

class UserError(Exception): pass


class UserValueError(UserError):
    def __init__(self, bad_val):
        self.message = f"'{bad_val}' can't be converted to an integer"


def do_calc(calc_expr):
    try:
        left, op, right = calc_expr.split()
    except ValueError:
        raise UserError("Make sure there is one space between each element.")

    try:
        left = int(left)
    except ValueError as err:
        raise UserValueError(left) from err

    try:
        right = int(right)
    except ValueError as err:
        raise UserValueError(right) from err

    if op == "+":
        return left + right
    elif op == "-":
        return left - right
    elif op == "*":
        return left * right
    elif op == "/":
        return left / right
    else:
        raise UserError(f"{op} is not a supported operation.")


print("Enter a space-separated expression. Ex: 5 * 7")
running = True
while running:
    try:
        to_calc = input("# ")
        result = do_calc(to_calc)
    except UserValueError as err:
        print(err.message)
    except UserError as err:
        print(err)
    except ZeroDivisionError:
        print("I'm not willing to divide by zero")
    except KeyboardInterrupt:
        print("\nGoodbye!")
        running = False
    else:
        print(result)
    finally:
        print("Running finally...")
