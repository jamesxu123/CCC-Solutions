import math, statistics, sys
input = sys.stdin.readline
n = int(input())
points = []
for i in range(n):
    points.append(tuple([float(a) for a in input().split()]))
if len(set(points)) == 1:
    print(0)
else:
    lis = []
    lis2 = []
    minX = min([i[0] for i in points])
    minY = min([i[1] for i in points])
    maxX = max([i[0] for i in points])
    maxY = max([i[1] for i in points])
    Mid = ((minX+maxX)/2,(minY+maxY)/2)
    for a in points:
        if i != a:
            lis.append(((Mid[0]-a[0])**2+(Mid[1]-a[1])**2)**0.5)
            lis2.append((Mid,a))
    x,y = lis2[lis.index(max(lis))][0]
    x1,y1 = lis2[lis.index(max(lis))][1]
    h,k = ((x+x1)/2,(y+y1)/2)
    rs = [((i[0]-h)**2+(i[1]-k)**2)**0.5 for i in points]
    print(max(rs))
