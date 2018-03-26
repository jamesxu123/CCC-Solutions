import math
n = int(input())
tides = [int(a) for a in input().split()]
sorted_tides = sorted(tides)
if n % 2 != 0:
    num_low = math.ceil(n/2)
    num_high = n-num_low+1
else:
    num_low = math.ceil(n/2)
    num_high = n-num_low  
low_tides = sorted_tides[:num_low]
low_tides = low_tides[::-1]
high_tides = sorted_tides[num_high:]
order_of_tides = []
for i in range(max(num_high,num_low)):
    try:
        order_of_tides.append(low_tides[i])
        order_of_tides.append(high_tides[i])

    except:
        pass
print(" ".join([str(e) for e in order_of_tides]))
