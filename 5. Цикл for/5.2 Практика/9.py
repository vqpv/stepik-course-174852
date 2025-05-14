n = int(input())
k = int(input())

f_1, f_2, f_3 = 1, 1, 1

for i in range(1, n + 1):
    f_1 *= i

for j in range(1, k + 1):
    f_2 *= j

for i in range(1, n - k + 1):
    f_3 *= i

print(f_1 // (f_2 * f_3))
