totalcups,totalstones = [int(i) for i in input().split()]
cupvalues = [0 for i in range(totalcups)]
for i in range(totalstones):
    cup_index = int(input())
    cupvalues[cup_index] += 1
prefixSum = cupvalues[:]
for i in range(1,totalcups):
    prefixSum[i] += prefixSum[i-1]
q = int(input())
print(prefixSum)
for i in range(q):
    a,b = [int(c) for c in input().split()]
    if a == 0:
        print(prefixSum[b])
    else:
        print((prefixSum[b] - prefixSum[a-1]))
