A = int(input())
B = int(input())

print(*range(A - 1 + A % 2, B - 1, -2))
