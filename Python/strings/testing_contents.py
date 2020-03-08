"""python provides a ton of options to test string contents"""

print("e in yes:","e" in "yes")  # True
print("x in yes:","x" in "yes")  # False
print("count t:","A Test String".count("t"))
print("index e:","A Test String".index("e"))  # ValueError if not found
print("rindex e:","A Test String".rindex("e"))
print("find e:","A Test String".find("e"))   # -1 if not found
print("rfind e:","A Test String".rfind("e"))
print("startswith A Tes:","A Test String".startswith("A Tes"))
print("endswith ring:","A Test String".endswith("ring"))

print("isalnum:","ATestString".isalnum())
print("isalpha:","ATestString".isalpha())
print("isascii:","A Test String".isascii())
print("isdecimal:","3.14".isdecimal())
print("isdigt:","42".isdigit())
print("isidentifier print:","print".isidentifier())
print("isidentifier cheese:","cheese".isidentifier())
print("islower:","a test string".islower())
print("isupper:","A TEST STRING".isupper())
print("istitle:","A Test String".istitle())
print("isnumeric:","1337".isnumeric())
print("isprintable true:","A Test String".isprintable())
print("isprintable false:","A\tTest\nString".isprintable())
print("isspace:"," \t \n ".isspace())
