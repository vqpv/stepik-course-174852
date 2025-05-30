n = int(input())

a, b = 0, 0

while n != 0:
    if a < n:
        b, a = a, n
    elif b < n:
        b = n
    n = int(input())

print(b)
