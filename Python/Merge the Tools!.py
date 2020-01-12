def merge_the_tools(string, k):
    s = []
    p = str()
    for i in range(0,len(string),k):
        s.append(string[i:i+k])
    for j in s:
        z = list(j)
        p = p+z[0]
        for q in z:
            if q not in p:
                p = p + q
        print(p)
        p=""
        z = []





if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
