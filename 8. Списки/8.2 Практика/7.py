l = list(map(int, input().split()))
x = int(input())

c = 1

for i in range(len(l)):
    if x > l[i]:
        break
    c += 1

print(c)
