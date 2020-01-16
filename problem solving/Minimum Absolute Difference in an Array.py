from itertools import combinations
n = int(input())
arr = list(map(int,input().split()))
k = 100000000000
arr.sort()
for i in range(len(arr)-1):
    p = int(abs(arr[i]-arr[i+1]))
    if k > p :
        k = p
        if k == 0 :
            print(k)
            exit()
    
print(k)
