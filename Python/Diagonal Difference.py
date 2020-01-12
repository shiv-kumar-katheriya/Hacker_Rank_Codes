n = int(input().strip())
arr = []
sum1 = 0
sum2 = 0
for _ in range(n):
    arr.append(list(map(int, input().split())))
for i in range(n):
    sum1 += arr[i][i]
for i in range(n):
    sum2 += arr[i][n-i-1]
print(abs(sum1-sum2))
