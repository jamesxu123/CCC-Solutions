from itertools import combinations
import sys
input = sys.stdin.readline
n,k = [int(a) for a in input().split()]
letters = []
for i in range(k):
    letters.append(int(input()))
email = [0 for i in range(n)]
counter = 0
for i in letters:
    email[i-1] = 'C'
print(email)
