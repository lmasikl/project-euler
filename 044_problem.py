import timeit
        
def palindrom():
    MIN = 100
    MAX = 1000
    STR = str
    
    def is_palindrom(n):
        return n == n[::-1]
        
    max_n = 0
    for i in range(MAX-1, MIN-1, -1):
        for j in range(MAX-1, i-1, -1):
            p = i * j
            if p > max_n and is_palindrom(STR(p)):
                max_n = p
    print max_n
    
if __name__ == '__main__':
    print timeit.timeit("palindrom()", setup="from __main__ import palindrom", number=1)
