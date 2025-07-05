def is_prime(n):
    return len([i for i in range(2, n + 1) if n % i == 0]) == 1

n = int(input())

print(is_prime(n))
