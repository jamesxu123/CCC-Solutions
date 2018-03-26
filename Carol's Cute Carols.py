n = int(input())
gifts = [int(a) for a in input().split()]
target = sorted(gifts)[::-1]
counter = 0
start = gifts[0]
while 1:
    for i in range(len(gifts)-1):
        if gifts[i] < gifts[i+1]:
            temp = gifts[i+1]
            gifts[i+1] = gifts[i]
            gifts[i] = temp
            counter += 1
    if gifts == target:
        break
print(counter)
