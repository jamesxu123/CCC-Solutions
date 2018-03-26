import sys
numV = int(input())
villages = []
for i in range(numV):
    villages.append(int(input()))
villages = sorted(villages)
neighborhood = []
distances = []
for i in range(1,len(villages)-1):
    neighborhood.append([(villages[i-1]+villages[i])/2,(villages[i+1]+villages[i])/2])
for i in neighborhood:
    distances.append(i[1]-i[0])
print(round(min(distances),1))
