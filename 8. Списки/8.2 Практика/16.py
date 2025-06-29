result = "NO"
x = []
y = []

for _ in range(8):
    x_i, y_i= map(int, input().split())
    x.append(x_i)
    y.append(y_i)

for i in range(8):
    for j in range(i + 1, 8):
        if (x[i] == x[j] or y[i] == y[j]) or (abs(x[i] - x[j]) == abs(y[i] - y[j])):
            result = "YES"

print(result)
