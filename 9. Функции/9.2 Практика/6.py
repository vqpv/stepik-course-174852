from math import sqrt


def distance(x_1, y_1, x_2, y_2):
    return sqrt((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2)

a, b = float(input()), float(input())
c, d = float(input()), float(input())

print(distance(a, b, c, d))
