M = int(input())
N = int(input())
K = int(input())
map_of_city = [[0 for i in range(M)] for a in range(N)]
for i in range(K):
    x,y,R,B = [int(a) for a in input().split()]
    x = int((r**2-y**2)**0.5)
    for i in abs(x):
        
