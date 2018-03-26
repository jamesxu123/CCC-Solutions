N,M,K = [int(a) for a in raw_input().split()]
cake = [[0 for i in range(N)] for i in range(M)]
for i in range(K):
    sx,sy,ex,ey = [int(a) for a in raw_input().split()]
    for y in xrange(sy-1,ey):
        for x in xrange(sx-1,ex):
            cake[y][x] += 1
for i in xrange(int(input())):
    A,B,C,D = [int(a) for a in raw_input().split()]
    total = 0
    for x in xrange(A-1,C):
        for y in xrange(B-1,D):
            total += cake[y][x]
    print total
