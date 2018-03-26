import functools
dist = int(input())
m = [-1 for i in range(dist+1)]
n_clubs = int(input())
clubs = []
for i in range(n_clubs):
    clubs.append(int(input()))
##n_hits = {c:-1 for c in clubs}
def hit(n):
    lis = []
    if m[n] != -1:
        return m[n]
    if n == 0:
        return 0
    if n < 0:
        return 999999999999
    for i in clubs:
        lis.append(n-i)
    m[n] = 1+min([hit(i) for i in lis])
    return m[n]
##    return (1+min(hit(n-33),hit(n-66),hit(n-1)))
var = hit(dist)
if var == 999999999999+2:
    print('Roberta acknowledges defeat.')
else:
    print('Roberta wins in %d strokes.' %(var))
