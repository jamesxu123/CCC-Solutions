N,M,K = [int(a) for a in input().split()]
cake = [[0 for i in range(N)] for i in range(M)]
for i in range(K):
    sx,sy,ex,ey = [int(a) for a in input().split()]
    for y in range(sy-1,ey):
        for x in range(sx-1,ex):
            cake[y][x] += 1
##cake = cake[::-1]
##prefix = [a for a in cake]
##cake = cake[::-1]
##for b in range(len(prefix)):
##    for c in range(1,len(prefix[b])):
##        prefix[b][c] += prefix[b][c-1]
##for d in range(1,len(prefix)):
##    for e in range(len(prefix[d])):
##        prefix[d][e] += prefix[d-1][e]
Q = int(input())
for i in range(Q):
    A,B,C,D = [int(a) for a in input().split()]
    total = 0
    for x in range(A-1,C):
        for y in range(B-1,D):
            total += cake[y][x]
    print(total)
