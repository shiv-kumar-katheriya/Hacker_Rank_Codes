import math
n = int(input())
p = int(input())
f = int(p/2)
b = (n-p)/2
 
if f>=b:
    if n % 2 == 0:
        print(math.ceil(b))
    else :
        print(int((n-p)/2))
else:
    print(f)
