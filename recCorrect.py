import functools
@functools.lru_cache()
def rec(n):
    print(n)
    if n==0:
        return 0
    if n<0:
        return 10000000
    return (1+min(rec(n-6),rec(n-1),rec(n-15)))
while 1:
    print(rec(int(input())))
