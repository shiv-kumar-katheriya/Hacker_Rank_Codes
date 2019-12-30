s = input()
if s == '12:00:00AM':
    print("00:00:00")
elif s == '12:00:00PM':
    print('12:00:00')
else:
    z = int(s[:2])
    a = s[8:]
    #print(z,a)
    if a == 'PM':
        if z < 12:
            z += 12
            print(z,end="")
            print(s[2:8])
        else:
            print(s[:8])
    else:
        if z == 12:
            z = "00"
            print(z,end="")
            print(s[2:8])
        else: 
            print(s[:8])
