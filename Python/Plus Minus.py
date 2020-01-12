n = int(input())
arr = list(map(int, input().rstrip().split()))
pos = zero = neg = 0
for i in arr:
    if i > 0:
        pos += 1
    elif i < 0:
        neg += 1
    else:
        zero += 1
print ('%.6f'%(pos/n))
print('%.6f'%(neg/n))
print('%.6f'%(zero/n))
