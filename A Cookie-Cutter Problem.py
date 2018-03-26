import math, statistics
n = int(input())
points = []
for i in range(n):
    points.append(tuple([int(a) for a in input().split()]))
if len(set(points)) == 1:
    print(0)
else:
    ax = statistics.mean([i[0] for i in points])
    ay = statistics.mean([i[1] for i in points])
    dist = {float(math.hypot((ax-i[0]),(ay-i[1]))): i for i in points}
    d_from_center = [float(math.hypot((ax-i[0]),(ay-i[1]))) for i in points]
    d_from_center = sorted(d_from_center)[::-1]
    if len(points) == 2:
        print(d_from_center[0])
    else:
        a,b = dist[d_from_center[0]]
        c,d = dist[d_from_center[1]]
        h,k = [statistics.mean([a,ax]),statistics.mean([b+ay])]
        radi = math.hypot((a-ax),(b-ay))
        print(radi)
            

    
