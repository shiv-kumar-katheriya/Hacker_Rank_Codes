from itertools import product
z = list(map(int,input().split()))

b = z[0]
n = z[1]
m = z[2]
z1 = list(map(int,input().split()))
z2 = list(map(int,input().split()))
z = list(product(z1,z2))
x = 0
for i in z:
    if sum(i) <=  b :
        x = max(x,sum(i))
if x == 0:
    print(-1)
else:
    print(x)
        
        
