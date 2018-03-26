string = input()
typesofchar = set([i for i in string])
n_times = 0
if len(typesofchar) <= 2:
    print(0)
else:
    count = [string.count(i) for i in typesofchar]
    count = sorted(count)
    while 1:
        n_times += count.pop(0)
        if len(count) <= 2:
            print(n_times)
            break


