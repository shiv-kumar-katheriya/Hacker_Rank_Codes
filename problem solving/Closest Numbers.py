n = int(input())
arr = list(map(int,input().split()))
arr.sort() 
m1 = []
m2 = [] 
for i in range(1,n):
    j = i - 1
    m1.append(arr[i] - arr[j])
    m2.append((arr[j],arr[i]))
z = min(m1)
for i in range(len(m1)):
    if z == m1[i]:
        print(m2[i][0],m2[i][1],end=" ")

