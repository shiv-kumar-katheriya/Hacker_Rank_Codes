def minion_game(a):
    vowel = ["A","E","I","O","U"]
    STUART = 0
    KEVIN = 0
    for i in range(0,len(a)):
        if a[i] in vowel:
            KEVIN = KEVIN + len(a) - i
        else :
            STUART = STUART +  len(a) - i
    if STUART < KEVIN:
        print("Kevin",KEVIN)
    elif KEVIN < STUART : 
        print("Stuart",STUART)
    else :
        print("Draw")
  

if __name__ == '__main__':
    s = input()
    minion_game(s)

