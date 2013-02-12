"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import timeit

def pythagorean_triplet(x=900):
    for i in xrange(x, 1, -1):
        for j in xrange(i, 1, -1):
            for k in xrange(j, 1, -1):
                if (i + j + k == 1000) and (i**2 == j**2 + k**2):
                    print i * j * k

def v_2(c=71):
    for l in xrange(1, c+1):
        for u in xrange(1, c+1):
            for v in xrange(1, c+1):
                if v > u:
                    x = l + (v**2 - u**2)
                    y = l * 2 * v * u
                    z = 1 * (v**2 - u**2)
                    if (x == c) or (y == c) or (z == c):
                        print x, y, z

if __name__ == "__main__":
    print timeit.timeit(
        "pythagorean_triplet()", 
        setup="from __main__ import pythagorean_triplet", 
        number=1
    )
    print timeit.timeit(
        "v_2()", 
        setup="from __main__ import v_2", 
        number=1
    )
