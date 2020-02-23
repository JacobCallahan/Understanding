"""variables"""

# good names
age = 42
name = "steve"
address = "123 sesame st."

# bad names
a = 5
thisismysuperawesomevariablewithalongname = 17

# illegal names
# 99red_balloons = None  # can't start with numbers
# red-balloons = 99      # can't contain dashes
# red balloons = 99      # can't use spaces

# recommended patterns
normal = "A normal variable"
mutliple_words = "separate words with an underscore"
MyClassName = "Use 'came' casing for class names"
GLOBAL_VARIABLE = "Use all caps for global variables"
CONSTANT = "constants should also be capitalized"

# variable switching
hungry = True
hungry = False

# dynamic typing!
hungry = 7
hungry = "I am not currently hungry!"

# nicknaming
yell = print
yell("Hello, World!")
yell(hungry)

# scope
MY_AGE = 33
def no_change():
    MY_AGE = 45
    print("Age after: ", MY_AGE)

def yes_change():
    global MY_AGE
    MY_AGE -= 4
    print("Age after: ", MY_AGE)

def no_out_change():
    outer_var = "astronaut"
    def inner():
        outer_var = "fire truck"
        inner_var = "spy"
        print("I wanted to be a ", outer_var)
    inner()
    print("Most kids wanted to be a firefighter.")
    print("But I wanted to be a(n) ", outer_var)
    try:
        print("But being a ", inner_var, " could be cool")
    except:
        print("Too secret for me!")

def yes_out_change():
    outer_var = "astronaut"
    def inner():
        nonlocal outer_var
        outer_var = "fire truck"
        inner_var = "spy"
        print("I wanted to be a ", outer_var)
    inner()
    print("Most kids wanted to be a firefighter.")
    print("But I wanted to be a(n) ", outer_var)
    try:
        print("But being a ", inner_var, " could be cool")
    except:
        print("Too secret for me!")