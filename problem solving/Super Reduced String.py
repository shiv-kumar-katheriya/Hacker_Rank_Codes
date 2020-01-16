a = input()
i = 1
while i < len(a):
    j = i - 1
    if a[i] != a[j]:
        i = i + 1
        continue
    elif a[i] == a[j] :
        a = a[0:j] + a[i+1:]
        i = 1    
if len(a) == 0:
    print("Empty String")
else : 
    print(a) 
        
