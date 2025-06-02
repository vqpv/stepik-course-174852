a = int(input())
b = int(input())

c, m = 1, 1

while b != 0:
    if a == b:
        c += 1
        if c > m:
            m = c
    else:
        c = 1
    a = b
    b = int(input())

print(m)
