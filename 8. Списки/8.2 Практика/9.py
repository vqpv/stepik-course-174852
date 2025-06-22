lst = list(map(int, input().split()))

for i in range(len(lst) - 1):
    if i % 2 == 0:
        lst[i], lst[i + 1] = lst[i + 1], lst[i]

print(*lst)
