"""File input and output allows you to read from and write to disk"""

from os import name

# manual open and close
names_file = open("names.txt")
print(f"File name: {names_file.name}")
all_names = names_file.read()
print(all_names)
print("Reading more lines")
print(names_file.readline() or "end of file")
print(names_file.readline() or "end of file")
names_file.close()
print(f"File closed? {names_file.closed}")

# read all lines into a list
names_file = open("names.txt")
all_names = names_file.readlines()
print(f"{all_names=}")
print("Printing out one at a time")
for name in all_names:
    print(name, end="")
names_file.close()

# introducing the context manager
with open("names.txt") as names_file:
    print("Reading three names")
    print(names_file.readline(), end="")
    print(names_file.readline(), end="")
    print(names_file.readline(), end="")

# iterate line by line
with open("names.txt", "r") as names_file:
    print("Reading all names")
    for name in names_file:
        print(name, end="")

# writing to files
with open("new_file.txt", "w") as nf:
    nf.write("these lines ")
    nf.write("are not separated")
    nf.write("\nuse newlines to separate\n")
    nf.write("writelines will write more than one string:\n")
    nf.writelines(map(str, range(6)))
    nf.write("\nyou still need newline characters:\n")
    nf.writelines(map(lambda s: f"{s}\n", range(6)))

# working with binary files
with open("binary_file", "wb") as b_file:
    b_file.write(b"0123456789")
    bytes_written = b_file.write(b"qwertyuiop")
    print(f"We wrote {bytes_written} bytes to {b_file.name}!")
