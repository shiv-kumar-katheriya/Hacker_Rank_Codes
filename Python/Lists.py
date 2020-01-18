if __name__ == '__main__':
    a = list()
    com = list()
    for _ in range(int(input())):
        com = list(map(str,input().split()))
        if com[0] == 'insert':
            a.insert(int(com[1]),int(com[2]))
        elif (com[0] == 'print'):
            print(a)
        elif com[0] == 'pop':
            a.pop()
        elif com[0] ==  'append':
            a.append(int(com[1]))
        elif com[0] ==  'reverse' :
            a.reverse()
        elif com[0] == 'remove':
            a.remove(int(com[1]))
        elif com[0] == 'sort':
            a.sort()

        

