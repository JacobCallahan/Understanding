"""strings - immutable lists of characters (actually strings)"""

# creating strings
basic_string = "review my data types video for more string examples"

multi1 = "this is " \
         "all one " \
         "string"

multi2 = (
    "this is "
    "another "
    "string"
)

multi3 = """use triple quotes
if you want your string to
preserve newline characters"""

multi4 = """if you don't want \
newline characters in your multiline \
strings, use this character \
"""

# converting into strings
int_to_str = str(321684321)
list_to_string = str([1, 2, 3, 4])
dict_to_string = str({"1": 1, "2": 2, "3": 3})
joined = "~~~".join(["A", "Test", "String"])

# string literals
lit1 = "something \" else "
lit2 = "\\"
lit3 = "\n"
lit4 = "\t"

# types of strings
normal = "normal unicode string"
raw = r"raw \n doesn't \\ format \t literals"
byte = b"bytes"