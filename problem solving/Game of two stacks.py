def twoStacks(x, a, k):
    m1 = []
    m2 = []
    c = 0
    total  = 0
    for i in a :
        if total + i <= x:
            m1.append(i)
            c += 1
            total += i 
        else :   
            break
    count = c
    i = 0 
    z = len(k)        
    while z > i :
        if total + k[i]  <= x:
            m2.append(k[i])
            c += 1
            total += k[i]
            i += 1
            if count < c:
                count = c
        elif m1!= []:  
            q = m1.pop()
            total = total - q
            if total + k[i]  <= x:
                m2.append(k[i])
                total += k[i]
                i += 1               
            else :
                c -= 1
                continue
        else :
            break
    return count
    

g = int(input())
for q in range(g):
    nmx = input().split()
    n = int(nmx[0])
    m = int(nmx[1])
    x = int(nmx[2])
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = twoStacks(x, a, b)
    print(result)
