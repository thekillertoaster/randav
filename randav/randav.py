import random
import sys
from randav.parts import randint


class Randav:
    def __getattr__(self, name):
        # Use '__dict__' to check for custom attributes and avoid recursion
        if name in self.__dict__:
            return self.__dict__[name]
        elif hasattr(random, name):
            return getattr(random, name)
        else:
            raise AttributeError(f"{self.__class__.__name__!r} object has no attribute {name!r}")

    @staticmethod
    def randint(a, b):
        # Use randrange() instead of randint(): The randrange() function is faster than randint() as it doesn't have to
        # do the extra arithmetic to compute the random number.
        return randint(a, b)


_randav = Randav()
sys.modules[__name__] = _randav
