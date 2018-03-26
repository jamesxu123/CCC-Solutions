D = int(input())
Rtime = D%720
left_over = D-Rtime
count = 0
day = 0
for i in range(1,Rtime+1):
    a,b,c,d = [0,0,0,0]
    minutes = i%60
    hour = int((12+((i-minutes)/60)))
    if hour > 12:
        hour %= 12
    if len(str(hour)) == 1:
        b = hour
    else:
        a = int(str(hour)[0])
        b = int(str(hour)[1])
    if len(str(minutes)) == 1:           
        c = 0
        d = minutes
    else:
        c = int(str(minutes)[0])
        d = int(str(minutes)[1])
    if len(str(hour)) == 1:
        if c-b == d-c:
            count += 1
    else:
        if b-a == d-c and b-a == c-b:
            count += 1
if left_over != 0:
    for i in range(1,720):
        a,b,c,d = [0,0,0,0]
        minutes = i%60
        hour = int((12+((i-minutes)/60)))
        if hour > 12:
            hour %= 12
        if len(str(hour)) == 1:
            b = hour
        else:
            a = int(str(hour)[0])
            b = int(str(hour)[1])
        if len(str(minutes)) == 1:           
            c = 0
            d = minutes
        else:
            c = int(str(minutes)[0])
            d = int(str(minutes)[1])
        if len(str(hour)) == 1:
            if c-b == d-c:
                day += 1
        else:
            if b-a == d-c and b-a == c-b:
                day += 1
    count += day*(left_over/720)
print(int(count))
