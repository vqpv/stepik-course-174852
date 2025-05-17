a = int(input())
b = int(input())
c = int(input())
d = int(input())

count = 0

for i in range(a, b + 1):
    if i % d == c:
        count += 1

print(count)
