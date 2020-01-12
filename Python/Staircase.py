n = int(input())
j = n-1
for i in range(n):
    print(" "*j,end="")
    print("#"*(i+1))
    j -= 1
