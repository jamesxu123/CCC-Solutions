import sys, statistics
input = sys.stdin.readline
n = int(input())
lis = []
for i in range(n):
    lis.append(statistics.median([int(a) for a in input().split()]))
print(statistics.median(lis))
