n = int(input())
lis = []
for i in range(n):
    lis.append(int(input()))
lis = sorted(lis)[::-1]
mods = 0
while 1:
    lis[0] -= lis[1]
    mods += lis[1]
    del lis[1]
    lis = sorted(lis)[::-1]
    if len(lis) < 2:
        break
print(mods)
            
        
