from math import floor
L,x = [int(a) for a in input().split()]
l = L
count = 0
for i in range(L):
    l-=(1/x)
    count += 1
print(L-floor(l))
