from collections import Counter
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
z = Counter(arr)
k = []
for i,m in z.items():
    k.append(m)
l = max(k)
k = [] 
for i,m in z.items():
    if m == l:
        k.append(i)
print(min(k))



