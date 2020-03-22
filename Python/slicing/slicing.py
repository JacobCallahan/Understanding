"""slicing - sequencing for lists, tuples, strings and more"""
# format: sliceable_object[start:stop:step]

# basics
print("==== Basics ====")
slice_list = list(range(26))
print("slice_list:", slice_list)
print("5:15 -", slice_list[5:15])
print("20: -", slice_list[20:])
print(":10 -", slice_list[:10])
print("5:-10 -", slice_list[5:-10])
print("-10:20 -", slice_list[-10:20])
print("::2 -", slice_list[::2])
print("::-2 -", slice_list[::-2])
print("::-2 ::-1 -", slice_list[::-2][::-1])
print("::10 -", slice_list[::10])
print("10:20:2 -", slice_list[10:20:2])
print("10:20:-2 -", slice_list[10:20:-2])
print("20:10:-2 -", slice_list[20:10:-2])
print("string 13:18 -", "you can even slice strings"[13:18])
print("string ::-1 -", "you can even slice strings"[::-1])

# intermediate
print("==== Intermediate ====")
skip2 = slice(None, None, 3)
print("skip2:", skip2)
print("slice skip2:", slice_list[skip2])
print("slice_list:", slice_list)
slice_list[5:10] = [55, 56, 57]
print("5:10 = [55, 56, 57]")
print("slice_list:", slice_list)
slice_list[:5] = ['replaced']
print(":5 = ['replaced]")
print("slice_list:", slice_list)
slice_list[2::2] = "RSTUVWXYZ"
print("2::2 = 'RSTUVWXYZ'")
print("slice_list:", slice_list)

# advanced
print("==== Advanced ====")
class ArrayMaker:
    def __getitem__(self, data):
        print(data)
        if isinstance(data, slice):
            fill = [data.step] * data.start
            return [fill[:] for _ in range(data.stop)]

print(ArrayMaker()[3:5:"test"])

