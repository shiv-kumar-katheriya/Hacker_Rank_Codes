from itertools import combinations
n = list(map(int,input().split()))
k,n = n[1],n[0]
arr = list(map(int,input().split()))
z = combinations(arr,2)
count = 0
for i in z:
    if sum(i) % k == 0:
        count += 1
print(count)
