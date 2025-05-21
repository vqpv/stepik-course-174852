n = int(input())

c = 0

for i in range(1, n + 1):
    for _ in range(i):
        if c < n:
            if c + 1 == n:
                print(i)
            else:
                print(i, end=" ")
            c += 1
