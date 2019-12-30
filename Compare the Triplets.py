a = list(map(int,input().split()))
b = list(map(int,input().split()))
result = [0,0]
for i in range(len(a)):
    if a[i] > b[i] : 
        result[0] += 1
    elif a[i] < b[i]:
        result[1] += 1
    else : 
        pass
for i in result:
    print(i,end=" ")
