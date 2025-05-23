N = int(input())

c = 0

while 2 ** (c + 1) <= N:
    c += 1

print(c, 2 ** c)
