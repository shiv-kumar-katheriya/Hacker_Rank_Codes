from collections import Counter
n = int(input())
size =  list(map(int,input().split()))
no = int(input())
size = Counter(size)
p = list(size.keys())
m = list(size.values())
count = 0

for i in range(no):
    z = list(map(int,input().split()))
    if z[0] in p:
        q = p.index(z[0])
        if m[q] != 0:
            count +=  z[1]
            m[q] -= 1
    else :
        z = []
        continue
    
print(count)
