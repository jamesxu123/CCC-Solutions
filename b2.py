boo = False
lis = []
abc = int(input())
for i in [i for i in range(1,101)]:
    for b in [i for i in range(1,101)]:
        if i%b != 0:
            boo = True
        else: boo = False
    if boo == True:
        lis.append(i)
print(lis[:abc-1])
