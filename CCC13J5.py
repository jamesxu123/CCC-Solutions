t = int(input())
g = int(input())
games = []
points = [0,0,0,0]
n_games = [0,0,0,0]
for i in range(g):
    game = [int(a) for a in input().split()]
    games.append(game)
for i in games:
    if i[2] > i[3]:
        points[i[0]-1] += 3
    elif i[2] == i[3]:
        points[i[0]-1] += 1
        points[i[1]-1] += 1
    elif i[3] > i[2]:
        points[i[1]-1] += 3
for i in games:
    for a in range(1,5):
        if a in [i[0],i[1]]:
            n_games[a-1] += 1
if 


