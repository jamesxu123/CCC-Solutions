import functools
@functools.lru_cache()
def rec(n):
    m[0] = 0
    for i in range(1,n+1):
        t = 100000000000000000
        if i >=  1:
            t = min([m[i-1]+1,t])
        if i >=6:
            t = min([m[i-6]+1,t])
        if i >=15:
            t = min([m[i-15]+1,t])
        m[i] = t
    return m[n]
while 1:
    n = int(input())
    m = [-1 for i in range(n+1)]
    print(rec(n))
    print(m)
