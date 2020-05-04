"""Generators - functions that behave like iterators"""

# normal function
def make_list(stop):
    result = []
    for i in range(stop):
        result.append(i**3)
    return result


def gen_list(stop):
    for i in range(stop):
        yield i**3


big_list = [x**3 for x in range(1000000)]
big_gen = (x**3 for x in range(1000000))


def gen_demo():
    yield "This"
    yield "is"
    yield "a"
    yield "broken"
    yield "up"
    yield "sentence."

print("===== Gen Demo =====")
for word in gen_demo():
    print(word)

print(" ".join(gen_demo()))


from string import ascii_lowercase
def brute_force_list():
    output = []
    for a in ascii_lowercase:
        for b in ascii_lowercase:
            for c in ascii_lowercase:
                for d in ascii_lowercase:
                    output.append(f"{a}{b}{c}{d}")
    return output


def brute_force_gen():
    for a in ascii_lowercase:
        for b in ascii_lowercase:
            for c in ascii_lowercase:
                for d in ascii_lowercase:
                    yield f"{a}{b}{c}{d}"


# intermidiate
print("===== Intermidiate =====")
def intermidiate_gen():
    curr_num = 1
    while True:
        skip = yield curr_num
        if isinstance(skip, int):
            curr_num += skip
        else:
            curr_num += 1

int_gen = intermidiate_gen()
for num in int_gen:
    if not num % 7:
        int_gen.send(11)
    print(num)
    if num > 100:
        break

