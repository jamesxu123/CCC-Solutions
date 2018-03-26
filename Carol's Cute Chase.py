n,m = [int(a) for a in input().split()]
flights = []
for i in range(m):
    flights.append([int(a) for a in input().split()])
for f in flights:
    paths = {i+1:[] for i in range(m)}
    temp = flights[:]
    del temp[flights.index(f)]
    for a in temp:
        paths[a[0]].append(a[1])
    checking = paths[1]
    checked = []
    done = False
    while checking and n not in checked:
        newFlights = []
        for a in checking:
            if a != n and a not in checked:
                newFlights += [i for i in paths[a]]
            elif a == n:
                done = True
                break
        checked += checking
        checking = newFlights
    if done:
        print('YES')
    else:
        print('NO')
            
        
        
        
