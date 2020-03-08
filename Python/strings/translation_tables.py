"""translation tables are useful for mapping character changes (translations)"""

trans_table1 = "A Tesx Sxring".maketrans({"x": "t"})
trans_table2 = "A Tesx Sxring".maketrans("x", "t")
print(trans_table1)
print(trans_table2)


trans1 = "A Tesx Sxring".translate(trans_table1)
trans2 = "A Tesx Sxring".translate(trans_table2)
print(trans1)
print(trans2)
