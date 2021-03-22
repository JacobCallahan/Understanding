"""
Context managers provide a clean interace for obtaining and releasing resources
To do this, we add the magic methods __enter__ and __exit__
"""
from pathlib import Path

class TempFile:
    def __init__(self, filename=None):
        print("Entering init")
        if not filename:
            from random import sample
            from string import ascii_letters
            filename = "".join(sample(ascii_letters, 15))
        self.file = Path(filename)

    def __enter__(self):
        print("Entering enter...")
        self.file.parent.mkdir(parents=True, exist_ok=True)
        if self.file.exists():
            self.file.unlink()
        self.file.touch()
        return self.file.open("w")

    def __exit__(self, *args):
        print("Entering exit!")
        self.file.unlink()

# with TempFile() as tf:
#     tf.write("This is a test!\nThis file will be gone soon!")
#     tf.flush()
#     import time
#     time.sleep(20)


class Expect:
    def __init__(self, *exc_types, message=None):
        self.exc_tyes = exc_types
        self.message = message

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_message, exc_tb):
        if exc_type in self.exc_tyes:
            if self.message and self.message in exc_message.args:
                return True
            elif self.message:
                return
            return True
        raise Exception(f"Expected one of {self.exc_tyes} exceptions.")


from contextlib import contextmanager

@contextmanager
def expensive_resource():
    resource = ["this is a complicated method"]
    try:
        yield resource
    except KeyboardInterrupt:
        print("I handled this correctly")
    finally:
        resource[0] = "cleaned up"
