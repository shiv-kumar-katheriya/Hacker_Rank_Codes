from itertools import combinations
n = list(map(int,input().split()))
arr = list(map(int,input().split()))
arr.sort()
z = 0 
l = 0
r = 0
while r!= len(arr) : 
    re = arr[r] - arr[l]
    if re == n[1]:
        z += 1
        r += 1
        l += 1
    elif re < n[1]:
        r += 1
    else:
        l += 1
        if l == r:
            r += 1
print(z)
