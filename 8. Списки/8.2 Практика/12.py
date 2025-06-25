lst = list(map(int, input().split()))
k, C = map(int, input().split())

lst.append(C)

for i in range(len(lst) - 1, k, -1):
    lst[i] = lst[i - 1]

lst[k] = C

print(*lst)
