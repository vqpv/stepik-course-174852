from math import sqrt

a = int(input())

n = 0
s_1 = 0
s_2 = 0

while a != 0:
    n += 1
    s_1 += a
    s_2 += a ** 2
    a = int(input())

result = sqrt((s_2 - 2 * (s_1 / n) * s_1 + n * (s_1 / n) ** 2) / (n - 1))

print(round(result, 3))
