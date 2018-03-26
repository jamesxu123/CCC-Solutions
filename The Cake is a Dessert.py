N,M,K = [int(a) for a in input().split()]
cake = [[0 for i in range(N)] for i in range(M)]
for i in range(K):
    sx,sy,ex,ey = [int(a) for a in input().split()]
    for y in range(sy-1,ey):
        for x in range(sx-1,ex):
            cake[y][x] += 1
prefix = [a for a in cake]
for b in range(len(prefix)):
    for c in range(1,len(prefix[b])):
        prefix[b][c] += prefix[b][c-1]
for d in range(1,len(prefix)):
    for e in range(len(prefix[d])):
        prefix[d][e] += prefix[d-1][e]
print(prefix)
Q = int(input())
for i in range(Q):
    A,B,C,D = [int(a) for a in input().split()]
    if A == 1 and B == 1:
        print(prefix[D-1][C-1])
    elif A in [1] and B != 1:
        print(prefix[D-1][C-1] - prefix[B-2][-1])
    else:
        print(prefix[D-1][C-1] - prefix[B-1][C-2])
