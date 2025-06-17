l = input().split()

print(*[int(i) for i in l if int(i) % 2 == 0])
