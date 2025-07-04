def dividers(n):
    return [i for i in range(1, n + 1) if n % i == 0]

n = int(input())

print(*dividers(n))
