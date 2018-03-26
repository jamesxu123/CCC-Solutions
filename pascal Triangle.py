def pascal(x,y):
    if x == 0 or x == y:
        return 1
    else:
        return pascal(x,y-1) + pascal(x-1,y-1)
print(pascal(int(input()),int(input())))
