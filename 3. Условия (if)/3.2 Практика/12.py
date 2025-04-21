n_1, n_2, n_3, n_4 = int(input()), int(input()), int(input()), int(input())

x = abs(n_3 - n_1)
y = abs(n_4 - n_2)

if (x == 1 and y == 2) or (x == 2 and y == 1):
    print("YES")
else:
    print("NO")
