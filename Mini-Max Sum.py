arr = list(map(int, input().rstrip().split()))
arr.sort()
j = arr.pop()
print(sum(arr),sum(arr)+j-arr[0])
