lis = []
def rec(n):
    count = 0
    count += 1
    if n == 0 or n <0:
        return count
    else:
        return rec(n-6),rec(n-1),rec(n-15)
print(rec(18))
