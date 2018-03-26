n = int(input())
swifts = [int(a) for a in input().split()]
sema = [int(b) for b in input().split()]
prefix_swifts = swifts[:]
prefix_sema = sema[:]
same = False
for i in range(1,n):
    prefix_swifts[i] += prefix_swifts[i-1]
    prefix_sema[i] += prefix_sema[i-1]
for i in range(1,n+1):
    if prefix_swifts[-i] == prefix_sema[-i]:
        print(n+1-i)
        same = True
        break
if same == False:
    print(0)
