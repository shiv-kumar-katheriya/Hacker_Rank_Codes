from collections import Counter
n = int(input())
arr = list(map(int,input().split()))
arr.sort()
count = 0
z = Counter(arr)
for m in z.values():
    count = count + (m//2)
print(count)  
