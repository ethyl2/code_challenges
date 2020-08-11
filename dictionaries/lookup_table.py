"""
https://github.com/LambdaSchool/cs-module-project-hash-tables/tree/master/applications/lookup_table

Modify the code to build a lookup table so that it can finish running in under a minute.

There's no test file for this. It's counting to 50,000, so if it finishes before you give up, then you're golden.
"""
import math
import random
import time


def slowfun_too_slow(x, y):
    global factorial_lookup
    global pow_lookup

    if (x, y) in pow_lookup:
        v = pow_lookup[(x, y)]
    else:
        v = math.pow(x, y)

    if v in factorial_lookup:
        v = factorial_lookup[v]
    else:
        v = math.factorial(v)
    v //= (x + y)

    v %= 982451653

    return v


factorial_lookup = {}
answer_lookup = {}
pow_lookup = {}


def slowfun(x, y):
    """
    A rewrite of slowfun_too_slow() that produces the same
    output, but completes quickly instead of taking ages to run.
    """
    global answer_lookup
    if (x, y) in answer_lookup:
        return answer_lookup[(x, y)]
    else:
        answer = slowfun_too_slow(x, y)
        answer_lookup[(x, y)] = answer
        return answer


start_time = time.time()
# Do not modify below this line!
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
end_time = time.time()

print(end_time - start_time)
