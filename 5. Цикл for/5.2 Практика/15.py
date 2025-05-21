n = int(input())

s_1 = 0
s_2 = 0

for i in range(1, n + 1):
    s_1 += i

for _ in range(n - 1):
    s_2 += int(input())

print(s_1 - s_2)
