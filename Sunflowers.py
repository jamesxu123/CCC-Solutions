import sys
input = sys.stdin.readline
measures = []
num = int(input())
for i in range(num):
    measures.append([int(a) for a in input().split()])
allGood = True
columns = []
for i in range(num):
    columns.append([measures[a][i] for a in range(num)])
rows = []
for i in range(num):
    rows.append([measures[i][b] for b in range(num)])
for i in rows:
    if i != sorted(i):
        done = False
for i in columns:
    if i != sorted(i):
        done = False
if not allGood:
    while True:
    ##    columns = []
    ##    for i in [0,num-1]:
    ##        columns.append([measures[a][i] for a in range(num)])
    ##    rows = []
    ##    for i in range(1,num-1):
    ##        rows.append([measures[i][b] for b in range(num)])
        done = True
        nMeasures = [[-1 for i in range(num)] for i in range(num)]
        for x in range(num):
            for y in range(num):
                nMeasures[num-1-x][y] = measures[y][x]
        columns = []
        for i in range(num):
            columns.append([nMeasures[a][i] for a in range(num)])
        rows = []
        for i in range(num):
            rows.append([nMeasures[i][b] for b in range(num)])
        for i in rows:
            if i != sorted(i):
                done = False
        for i in columns:
            if i != sorted(i):
                done = False
        measures = nMeasures
        if done:
            break
    for i in nMeasures:
        print(' '.join([str(a) for a in i]))
else:
    for i in measures:
        print(' '.join([str(a) for a in i]))
