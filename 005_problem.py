import timeit

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
    
def division(MAX=20):
    N = MAX * 2 if MAX > 2 else MAX
    dividers = range(1, MAX+1)
    while True:
        divided = True
        for divider in dividers:
            if not (N % divider == 0):
                divided = False
                break
        if divided:
            break
        N += MAX
    print N
    
if __name__ == '__main__':
    print timeit.timeit("division()", setup="from __main__ import division", number=1)
