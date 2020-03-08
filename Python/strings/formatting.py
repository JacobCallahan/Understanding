"""string formatting allows you to inject data"""

name = 'Jake'
old_style = "my name is %s" % name
old_style2 = "My Name: %(name)s \nFavorite Number: %(num)d" % {"name": name, "num": 5}
formatted = "A {} String".format("Test")
formatted2 = "A {var1} String with {var2}".format(var1="test", var2="formatting")
map_format = "{p1} asd {p2} lijwoe {p3}".format_map({"p1": "A", "p2": "Test", "p3": "String"})
f_string = f"my name is {name}"

print("old_style:", old_style)
print("old_stye2:", old_style2)
print("formatted:", formatted)
print("formatted2", formatted2)
print("map_format:", map_format)
print("f_string", f_string)
