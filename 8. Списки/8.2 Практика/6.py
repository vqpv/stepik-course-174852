l = list(map(int, input().split()))

maximum = l[0]
index = 0

for i in range(len(l)):
    if l[i] > maximum:
        maximum = l[i]
        index = i

print(maximum, index)
