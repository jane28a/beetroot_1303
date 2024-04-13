from math import pi
from functools import partial

def volume(r, h):
    return r**2 * h * pi

if __name__ == "__main__":
    volume_3 = partial(volume, r=3)
    print(volume(4, 6))
    print(volume_3(8))
