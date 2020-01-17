from collections import Counter
n = int(input())
size =  list(map(int,input().split()))
no = int(input())
size = Counter(size)
p = list(size.keys())
print(p)
##for i in range(no):
##    z = list(map(int,input()))

