l = list(map(int, input().split()))

for i in range(len(l) - 1):
    if l[i] * l[i + 1] > 0:
        print(l[i], l[i + 1])
        break
