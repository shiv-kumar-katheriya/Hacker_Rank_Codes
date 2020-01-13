loc = list(map(int,input().split()))
q = list(map(int,input().split()))
size = list(map(int,input().split()))
m = list(map(int,input().split()))
n = list(map(int,input().split()))
c=0
for i in m:
    if (i+q[0])<=loc[1] and (i+q[0])>=loc[0]:
        c += 1
print(c)
c=0 
for i in n:
    if (i+q[1])<=loc[1] and (i+q[1])>=loc[0]:
        c += 1
print(c)
