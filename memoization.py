m = [-1 for i in range(100000)]
def rec(n):
    if m[n] != -1:
        return m[n]
    if n==0:
        return 0
    if n<0:
        return 10000000
    m[n] = (1+min(rec(n-6),rec(n-1),rec(n-15)))
    return m[n]
while 1:
    print(rec(int(input())))
