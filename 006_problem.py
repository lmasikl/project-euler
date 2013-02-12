import timeit

"""
The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and 
the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def difference_sum_sq_and_sq_sum(n):
    return sum(xrange(1, n+1))**2 - sum(map(lambda x: x**2, xrange(1, n+1)))
    
def difference_sum_sq_and_sq_sum_better(n):
    """
    Better because it math formula, only arifmetic
    """
    return (n * (n + 1) / 2)**2 - (n * (n + 1) * (2 * n + 1) / 6)
    
if __name__ == '__main__':
    print timeit.timeit(
        "print difference_sum_sq_and_sq_sum(100)", 
        setup="from __main__ import difference_sum_sq_and_sq_sum", 
        number=1
    )
    print timeit.timeit(
        "print difference_sum_sq_and_sq_sum_better(100)", 
        setup="from __main__ import difference_sum_sq_and_sq_sum_better", 
        number=1
    )
    
