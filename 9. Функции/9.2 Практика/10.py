def arithmetic_progression(a, d, n):
    return (2 * a + (n - 1) * d) * n // 2

a, d, n = [int(x) for x in input().split()]

print(arithmetic_progression(a, d, n))
