from itertools import combinations
from statistics import median
n,x = [int(a) for a in input().split()]
spikes = [int(a) for a in input().split()]
lis = list(combinations(spikes,3))
counter = 0
for i in lis:
    z = sorted(i)
    if z[1] == x:
        counter += 1
print(counter)
