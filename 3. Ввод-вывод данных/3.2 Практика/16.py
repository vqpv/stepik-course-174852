n = int(input())
k = int(input())
m = int(input())

x = k - k % m
y = n - k

print((k // m) * (y // x + 1))
