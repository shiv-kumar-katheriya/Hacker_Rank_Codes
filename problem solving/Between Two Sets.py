n = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))
m = n[0]
n = n[1]
l = []
count = 0
a.sort()
b.sort()
for i in range( a[m-1] , b[0] + 1 ):
    c = 0
    for j in a:
        if i % j == 0:
            c += 1
        else:
            break
    if c == m:
        l.append(i)

for i in l:
    c = 0
    for j in b:
        if j % i == 0:
            c += 1
        else:
            break
    if c == n:
        count += 1
print(count)
    
