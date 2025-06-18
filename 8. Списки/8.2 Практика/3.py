l = input().split()

print(*[int(l[i]) for i in range(1, len(l)) if int(l[i]) > int(l[i - 1])])
