n, k = map(int, input().split())

result = ["I"] * n

for i in range(k):
    l_i, r_i = map(int, input().split())
    for j in range(n):
        if result[j] == "I" and j in range(l_i - 1, r_i):
            result[j] = "."

print("".join(result))
