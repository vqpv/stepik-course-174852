from math import ceil

h = int(input())
a = int(input())
b = int(input())

if a >= h:
    print(1)
else:
    print(ceil((h - a) / (a - b)) + 1)
