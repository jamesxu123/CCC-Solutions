a,b = [int(i) for i in input().split()]
c,d = [int(i) for i in input().split()]
t = int(input())
dx = abs(a-c)
dy = abs(b-d)
dist = dx+dy
if dist <= t and (t-dist) % 2 == 0:
    print('Y')
else:
    print('N')
