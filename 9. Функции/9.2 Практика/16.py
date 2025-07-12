def lcm(a, b):
    r = a * b
    for i in range(min(a, b), r + 1):
        if i % a == 0 and i % b == 0:
            return i
    return r

a, b = [int(x) for x in input().split()]

print(lcm(a, b))
