from itertools import combinations

def icecreamParlor(m, arr):
    z = combinations(arr,2)
    for i in z:
        if sum(i) == m:
            break
    q = []
    q.extend(i)
    for i in range(len(q)):
        p = arr.index(q[i])
        q[i] = p + 1
        arr[p] = "-"
    return q

if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        m = int(input())
        n = int(input())
        arr = list(map(int, input().rstrip().split()))
        result = icecreamParlor(m, arr)
        print(' '.join(map(str, result)))
