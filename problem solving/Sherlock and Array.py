def balancedSums(n,arr):
    if n == 1:
        return "YES"
    else : 
        le = 0
        re = sum(arr[1:])
        for i in range(n-1):
            if le == re:
                return "YES"
            else:
                le += arr[i]
                re -= arr[i+1] 
        else:
            return "NO"



if __name__ == '__main__':
    T = int(input().strip())
    for T_itr in range(T):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        print(balancedSums(n,arr))

