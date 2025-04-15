year = int(input())

n_1 = 4
n_2 = 100
n_3 = 400

if (year % n_1 == 0 and year % n_2 != 0) or (year % n_3 == 0):
    print("YES")
else:
    print("NO")
