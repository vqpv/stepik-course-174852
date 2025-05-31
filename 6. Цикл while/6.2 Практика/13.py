n = int(input())

a = 0
c = 1

while n != 0:
    if a < n:
        a = n
        c = 1
    elif a == n:
        c += 1
    n = int(input())

print(c)
