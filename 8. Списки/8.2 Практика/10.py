lst = list(map(int, input().split()))

minimum = lst.index(min(lst))
maximum = lst.index(max(lst))

lst[minimum], lst[maximum] = lst[maximum], lst[minimum]

print(*lst)
