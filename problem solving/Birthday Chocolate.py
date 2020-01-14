n = int(input())
arr = list(map(int,input().split()))
a = list(map(int,input().split()))
d = a[0]
m = a[1]
count = 0
for i in range(n - m + 1 ):

    if sum(arr[i:(m+i)]) == d:
        count += 1
print(count)
