n_1, n_2, n_3 = int(input()), int(input()), int(input())

if n_1 == n_2 and n_1 == n_3:
    print(3)
elif n_1 == n_2 or n_1 == n_3 or n_2 == n_3:
    print(2)
else:
    print(0)
