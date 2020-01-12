from itertools import product
n = list(map(int,input().split()))
m = list(map(int,input().split()))
j = product(n,m)
for i in j:
    print(i,end=" ")
