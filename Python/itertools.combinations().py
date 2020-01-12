from itertools import combinations
a,b = input().split()
a = list(a)
a.sort()
a = "".join(a)
for i in range(1,int(b)+1):
    z =  combinations(a,i)
    m = list() 
    for j in z:
        print("".join(j))


