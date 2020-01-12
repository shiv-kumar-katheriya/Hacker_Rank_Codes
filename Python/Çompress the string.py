from itertools import groupby
n = input()
n = list(n)
for (key,group) in groupby(n):
    print((len(list(group)),int(key)),end=" ")
