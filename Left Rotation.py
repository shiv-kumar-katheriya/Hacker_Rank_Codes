n = list(map(int,input().split()))
arr = list(map(int,input().split()))
t = []
for i in range(n[1]):
    a = arr.pop(0)
    arr.append(a)
for i in arr:
    print(i,end=" ")
