def power(a, n):
    result = 1.0
    for _ in range(n):
        result *= a
    return round(result, 3)

a = float(input())
n = int(input())

print(power(a, n))
