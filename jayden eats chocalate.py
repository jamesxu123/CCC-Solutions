from math import *
numSquares = int(input())
x,y,z = [int(a) for a in input().split()]
minChoices = sorted([x,y,z])
total = 0
boo = True
count = 0
while True:
    if total + minChoices[0] == total:
        boo = False
        break
    if total + minChoices[0] > numSquares and total + minChoices[0] != numSquares:
        total -= minChoices[0]
        print(True)
        break
    total += minChoices[0]
    count += 1
while True and boo:
    if total + minChoices[1] == total:
        boo = False
        break
    if total + minChoices[1] > numSquares and total + minChoices[1] != numSquares:
        break
    total += minChoices[1]
    count += 1

while True and boo:
    if total + minChoices[2] == total:
        boo = False
        break
    if total + minChoices[2] > numSquares and total + minChoices[2] != numSquares:
        break
    total += minChoices[2]
    count += 1

print(total)
