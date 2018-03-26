arr = [0 for i in range(3125)]#3125 = 5^5
##where arr[a][b][c][d][e]
a,b,c,d,e =[1,2,3,4,5]
print(arr[a*5**4+b*5**3+c**2+d*5+e])
