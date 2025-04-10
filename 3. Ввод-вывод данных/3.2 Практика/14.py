x_1 = int(input())
y_1 = int(input())
a_1 = int(input())
b_1 = int(input())
x_2 = int(input())
y_2 = int(input())

c_time = x_1 * 60 + y_1
n_time = x_2 * 60 + y_2
o_time = a_1 * 60 + b_1

r_time = (n_time - c_time) * 2

result_time = o_time + r_time

print(result_time // 60 % 24, result_time % 60)
