s = input()
z = len(s)/3
z = 'SOS'*int(z)
count = 0
for i in range(len(z)):
    if s[i] != z[i]:
        count += 1
print(count)
