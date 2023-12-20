"""You can also inherit from named tuples similar to normal classes"""
from collections import namedtuple


class RGB(namedtuple("RGB", "red green blue")):
    @property
    def r(self):
        return self.red

    @property
    def g(self):
        return self.green

    @property
    def b(self):
        return self.blue

    @property
    def hex(self):
        return "#{:02X}{:02X}{:02X}".format(self.r, self.g, self.b)


cyan = RGB(0, 255, 255)


RGBA = namedtuple("RGBA", RGB._fields + ("alpha",))

cyan2 = RGBA(0, 255, 255, 128)
