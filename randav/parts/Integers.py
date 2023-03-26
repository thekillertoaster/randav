import random


# Use randrange() instead of randint(): The randrange() function is faster than randint() as it doesn't have to
# do the extra arithmetic to compute the random number.
def randint(a, b): return random.randrange(a, b + 1)
