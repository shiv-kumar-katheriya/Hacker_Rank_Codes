from itertools import combinations
def pairs(n,k, arr):
    count = 0
    arr.sort()
    i = 0
    j= 1
    while j <= n-1:
        c = arr[j] -  arr[i]  
        if c == k:
            count += 1
            j += 1
        elif c < k :
            j += 1
        else :
            i += 1
    return count 
if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))
    result = pairs(n , k, arr)
    print(result)

