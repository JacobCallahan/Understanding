"""there are many methods to alter strings"""

print("upper:", "A Test String".upper())
print("lower:", "A Test String".lower())
print("capitalize:", "a test string".capitalize())
print("title:", "a test string".title())
print("swapcase:", "A Test String".swapcase())
print("casefold:", "A Test String".casefold())

print("ljust 20:", "A Test String".ljust(20, "x"))
print("rjust 20:", "A Test String".rjust(20, "x"))
print("center 20:", "A Test String".center(20, "x"))
print("zfill 20:", "A Test String".zfill(20))
print("zfill 2:", str(1).zfill(2))
print("zfill 2:", str(10).zfill(2))
print("zfill 2:", str(100).zfill(2))

print("expantabs 16:", "A\tTest\tString".expandtabs(16))
print("replace x->t:", "A Tesx Sxring".replace("x", "t"))
print("replace Something->Test:", "A Something String".replace("Something", "Test"))
print("lstrip:", "   A Test String   ".lstrip())
print("rstrip:", "   A Test String   ".rstrip())
print("strip:", "   A Test String   ".strip())

print("encode:", "A Test String".encode())
