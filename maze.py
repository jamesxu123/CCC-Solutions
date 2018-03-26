t = int(input())
for i in range(t):
    r = int(input())
    c = int(input())
    ops = []
    for i in range(r):
        op = list(input())
        ops.append(op)
    level = 1
    start = (0,0)
    end = (r-1,c-1)
    checking = [start]
    checked = []
    moves = {'+':[(1,0),(0,1),(-1,0),(0,-1)],
             '-':[(1,0),(-1,0)],
             '|':[(0,1),(0,-1)],
             '*':[]}
    while checking and end not in checked:
        newItems = []
        for a in checking:
            if a not in checked and 0<=a[0]<r and 0<=a[1]<c and ops[a[0]][a[1]] != '*':
                for b in moves[ops[a[0]][a[1]]]:
                    if 0<=a[0]+b[0]<r and 0<=a[1]+b[1]<c:
                        newItems.append([a[0]+b[0],a[1]+b[1]])
        checked += checking
        checking = newItems
        level += 1
    print(level)
