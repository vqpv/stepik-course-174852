def gcd(a, b):
    i = a
    while i != 0:
        if a % i == 0 and b % i == 0:
            return i
        i -= 1
    return i

a, b = [int(x) for x in input().split()]

print(gcd(a, b))
