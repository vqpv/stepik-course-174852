lst = list(map(int, input().split()))

c = 1

for i in range(len(lst) - 1):
    if lst[i] != lst[i + 1]:
        c += 1

print(c)
