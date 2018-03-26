n = int(input())
k = int(input())
shifty = n
for i in range(1,k+1):
    shifty += n * (10**i)
print(shifty)
