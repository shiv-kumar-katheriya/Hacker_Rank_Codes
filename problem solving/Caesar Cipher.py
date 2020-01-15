import string
n = int(input())
s = input()
k = int(input())
if k > 26:
    k %= 26  
a = ""
al = " abcdefghijklmnopqrstuvwxyz"
for i in s:
    if i in string.ascii_letters:
        if al.find(i) != -1:
            z = al.find(i) + k
            if z > 26:
                z %= 26  
            i = al[z]               
        else:
            z = al.find(i.lower()) + k
            if z > 26:
                z %= 26
            i = al[z].upper()    
    a = a + i 
print(a)
        
