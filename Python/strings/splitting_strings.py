"""string splitting is allows you to break apart strings"""

print("split:", "A Test String".split())
print("split t:", "A Test String".split("t"))
print("rsplit:", "A Test String".rsplit())
print("partition t:", "A Test String".partition("t"))
print("rpartition t:", "A Test String".rpartition("t"))
print("splitlines none:", "A Test String".splitlines())
print("splitlines some:", "A\nTest\nString".splitlines())
