hull,islands,num_routes = [int(a) for a in input().split()]
routes = [{} for i in range(islands)]
for i in range(num_routes):
    a,b,t,h = [int(a) for a in input().split()]
    routes[a-1].setdefault(b-1,[]).append((t,h))
    routes[b-1].setdefault(a-1,[]).append((t,h))
start,dest = [int(a-1) for a in input().split()]

print(routes)
INF = 10**10
distance = [[INF for i in range(200+1)] for n in range(islands)]


