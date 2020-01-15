def hackerrankInString(s):
    c = "hackerrank"  
    k = 0
    a = len(s)
    for i in c:
        if k != -1 and i in s[k:] :
            k = s.find(i,k)
            if k != -1:
                k += 1
        else :
            return "NO"
    else : return "YES"
        
if __name__ == '__main__':
    q = int(input())
    for q_itr in range(q):
        s = input()
        result = hackerrankInString(s)
        print(result)

