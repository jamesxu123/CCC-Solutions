import sys
input = sys.stdin.readline
n = int(input())
boards = sorted([int(a) for a in input().split()])
combo = []
while 1:
    small = boards.pop(0)
    large = boards.pop(-1)
    combo.append(small+large)
    if len(boards) < 2:
        break
for i in boards:
    if i == 
