n = int(input())

a, b = 0, 1
c = 0

while n > a:
    a, b = b, a + b
    c += 1

if n == a:
    print(c)
else:
    print(-1)
