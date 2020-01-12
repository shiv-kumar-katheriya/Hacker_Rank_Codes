n1 = int(input())
st1 = []
for _ in range(n1):
    st1.append(input())
n2 = int(input())
st2 = []
for _ in range(n2):
    st2.append(input())
for n in st2:
    print(st1.count(n))
