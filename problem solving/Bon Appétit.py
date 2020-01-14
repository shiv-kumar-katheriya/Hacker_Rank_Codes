n = list(map(int,input().split()))
k = n[1]
n = n[0]
arr = list(map(int,input().split()))
b = arr.copy()
bill = int(input())
arr.remove(arr[k])
c = sum(arr)/2
if c == bill:
    print("Bon Appetit")
else:
    print(bill-int(c))
