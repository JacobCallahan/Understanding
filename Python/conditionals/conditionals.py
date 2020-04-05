"""if/elif/else - basic flow control"""

if True:
    print("This will always pass")

if False:
    print("This will never pass")
else:
    print("But this will")

if 1 == 2:
    print("== means 'these are equal?'")
elif "a" != "A":
    print("!= means 'these are not equal?'")

if True is 1:
    print("'is' means they are the same object")
elif True == 1:
    print("True isn't 1, but True equals 1")
else:
    print("False equals 0 as well")

if [] or "" or {} or None:
    print("Empty iterables will not pass")
elif ["test"] and 2 and "yes":
    print("but ones with values will")

if not "else":
    print("You can invert a 'truthy' value")
elif not 1 == 2:
    print("So false checks then become true")
elif "test" is not None:
    print("this makes some checks very easy to read")

