lst = list(map(int, input().split()))

last_num = lst[-1]

for i in range(len(lst) - 1, 0, -1):
    lst[i] = lst[i - 1]

lst[0] = last_num

print(*lst)
