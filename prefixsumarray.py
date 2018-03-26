def prefix(a,b,lis):
    psa = lis
    for i in range(len(lis)):
        psa[i] += psa[i-1]
    return psa[a]-psa[b]
lis = [int(a) for a in range(1000)]
h = prefix(2,5,lis)
print(h)
