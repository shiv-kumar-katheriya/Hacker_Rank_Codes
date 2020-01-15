def pangrams(s):

    lo = "abcdefghijklmnopqrstuvwxyz "
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    qu = [0]*27
    for i in s:
        if i in lo or i in up:
            if lo.find(i) != -1:
                qu[lo.find(i)] += qu[lo.find(i)] + 1
            else :
                qu[up.find(i)] += qu[up.find(i)] + 1
    if all(qu) == True:
        return "pangram"
    else:
        return "not pangram"

if __name__ == '__main__':
    s = input()
    result = pangrams(s)
    print(result)
