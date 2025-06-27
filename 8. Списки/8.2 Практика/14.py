lst = list(map(int, input().split()))

c = 0
len_lst = len(lst)

for i in range(len_lst):
    for j in range(i + 1, len_lst):
        if lst[i] == lst[j]:
            c += 1

print(c)
