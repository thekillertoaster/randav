import random
import sys


class Randav:
    def __getattr__(self, name):
        # Use '__dict__' to check for custom attributes and avoid recursion
        if name in self.__dict__:
            return self.__dict__[name]
        elif hasattr(random, name):
            return getattr(random, name)
        else:
            raise AttributeError(f"{self.__class__.__name__!r} object has no attribute {name!r}")


    def randint(self, a, b):
        # Your custom implementation for randint
        return a + int((b - a + 1) * random.random())


_randav = Randav()
sys.modules[__name__] = _randav
