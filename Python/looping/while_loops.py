"""while loops: loop until condition isn't true"""

print("===== loop until 5 =====")
num = 0
while num <= 4:
    print(num)
    num += 1
else:
    print(f"num is now > 4: {num}")

print("===== loop until 5? =====")
num = 0
while num >= 4:
    print(num)
    num += 1
else:
    print("num was never >= 4")

print("===== loop 'test' without 't' =====")
word, pos = "test", 0
while pos < len(word):
    if word[pos] == "t":
        pos += 1
        continue
    print(word[pos])
    pos += 1
else:
    print("reached the end of the word")

print("===== infinite loop with break =====")
word, pos = "test", 0
while True:
    print(word[pos])
    if pos + 1 == len(word):
        break
    pos += 1
else:
    print("reached the end of the word")